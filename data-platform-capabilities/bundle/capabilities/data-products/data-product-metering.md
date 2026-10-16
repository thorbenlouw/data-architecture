---
type: Capability
id: data-product-metering
title: Data product usage metering
description: Measure how much each consumer uses a data product so it can be billed, charged back or capped.
aliases: [consumption metering, data monetisation billing]
broader: [data-products]
related: [cost-attribution, data-marketplace, usage-metadata, spend-controls, external-data-sharing]
depends_on: [system-telemetry]
tags: [data-products]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Metering counts consumption per consumer and per product, in units that fit how the product is delivered: queries run, rows or bytes read, API calls, compute time used by the consumer's queries, or active seats. The platform collects these events from query history, access logs and API gateways, ties each one to a consumer identity and a product, and totals them into usage records for each billing period. For a dataset read by three departments, metering might show that one department causes 70% of the scanning.

It serves three purposes: billing external customers of commercial data products, charging internal consumers for what they use, and enforcing quotas or tiered plans. It also tells producers which products are valued and which can be retired. It differs from cost attribution, which allocates the platform's own spend to teams; metering measures use of a product, which may be priced independently of what it costs to run.

# Key considerations

- Choose units consumers can understand and predict. Bytes scanned is easy to measure but hard for consumers to forecast; per-call or per-seat units are easier to budget.
- When consumers query shared data with their own compute, as with many sharing protocols, the producer may see little of the usage. Check what the platform reports back to producers.
- Usage records that feed invoices need the accuracy and audit trail of financial data, including handling for late events, corrections and disputes.
- Identify consumers by named service or person, not by shared accounts, or usage cannot be attributed.

# Questions to ask

- Will usage be invoiced to external customers, charged back internally, or only reported?
- Which unit of consumption best reflects the value consumers get from the product?
- Do consumers query with their own compute or the producer's?
- Must consumers be capped or throttled when they exceed their plan?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data products](data-products.md) |
| Broader | [Data products](data-products.md) |
| Related | [Budgets and spend controls](../platform-operations/spend-controls.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Data marketplace](../data-sharing/data-marketplace.md), [External data sharing](../data-sharing/external-data-sharing.md), [External user and tenant identity](../security/external-identity.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |
| Depends on | [Usage and system telemetry](../platform-operations/system-telemetry.md) |

# Where it appears

- **Use cases:** [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from)
- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Data products](../../maturity/track-data-products.md) (from level 4, Measured) · [FinOps](../../maturity/track-finops.md) (from level 4, Measured)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 14 Cost Metrics (Data and technical architecture) · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Pricing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Data Exchange](../../technologies/aws/aws-data-exchange.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Apigee](../../technologies/google-cloud/gcp-apigee.md), [BigQuery sharing](../../technologies/google-cloud/gcp-bigquery-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../../technologies/snowflake/snowflake-listings.md) |
