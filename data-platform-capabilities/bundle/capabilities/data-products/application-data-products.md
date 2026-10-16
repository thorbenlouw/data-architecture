---
type: Capability
id: application-data-products
title: Vendor-supplied application data products
description: Use governed, documented datasets that business application vendors publish and maintain, instead of building extraction.
aliases: [zero-copy application data]
broader: [data-products, external-data-sharing]
related: [saas-connectors, packaged-analytics, data-usage-rights, database-replication]
tags: [data-products]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Rather than extracting hundreds of raw ERP, CRM or HR tables and reverse-engineering their joins and codes, the customer receives, for example, a documented sales order line dataset with business-friendly names, resolved codes and the vendor's own meaning attached, kept current as the application changes. Delivery is often by zero-copy sharing into the customer's platform or through a managed replica.

It matters because extraction from complex applications is expensive, fragile across upgrades, and sometimes limited by licence terms or API quotas. The vendor knows its data model best and can keep the dataset stable when internals change. The trade-offs are coverage, since not every table or custom field may be exposed, dependence on the vendor's roadmap and pricing, and fit with your own modelling standards. It differs from SaaS connectors, which copy raw application objects, and from packaged analytics, which adds metrics and dashboards on top.

# Key considerations

- Check coverage of custom fields and objects, which most organisations rely on and vendors often omit.
- Read the licence terms. Some vendors restrict extraction or charge for access to their data outside the application.
- Confirm freshness, history retention and change tracking, which affect incremental processing downstream.
- Map vendor definitions to your own master data and metric definitions before building on them.

# Questions to ask

- Which business applications are hardest and most costly to extract from today?
- Do your application vendors offer governed datasets, and what do they cover?
- Would vendor-defined meanings conflict with your own definitions?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data products](data-products.md) |
| Broader | [Data products](data-products.md), [External data sharing](../data-sharing/external-data-sharing.md) |
| Related | [Data licensing and usage rights](../governance/data-usage-rights.md), [Database replication and mirroring](../ingestion-integration/database-replication.md), [Packaged analytics content](../analytics-bi/packaged-analytics.md), [SaaS application connectors](../ingestion-integration/saas-connectors.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from)
- **Maturity tracks:** [Data products](../../maturity/track-data-products.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Fusion Data Intelligence](../../technologies/oracle/oracle-fusion-data-intelligence.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud data products](../../technologies/sap/sap-bdc-data-products.md) |
