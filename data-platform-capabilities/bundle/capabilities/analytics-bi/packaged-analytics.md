---
type: Capability
id: packaged-analytics
title: Packaged analytics content
description: Use prebuilt models, metrics and dashboards for a business domain that a vendor delivers and updates.
aliases: [industry data models, insight apps]
broader: [analytics-bi]
related:
- application-data-products
- metric-definitions
- semantic-layer
- saas-connectors
- enterprise-planning
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An order-to-cash package, for example, might include tables that reshape a standard ERP's sales and invoicing data, metrics such as days sales outstanding, and dashboards for the collections team. The organisation installs the package, maps it to its own source systems and configuration, and extends it with local logic. The vendor ships updates as the source application and the content evolve.

Packages shorten the time to first results for well-understood processes whose data structure is set by a commercial application, such as finance, procurement, HR or supply chain. The trade-off is fit and upgrade effort: the more a package is customised, the harder it is to take vendor updates, and the less closely it matches local definitions. It differs from vendor-supplied application data products, which deliver governed datasets; packaged analytics adds metrics and dashboards on top.

# Key considerations

- Measure fit against your own processes and source configuration before committing. Heavy customisation erodes the value of updates.
- Keep local extensions separate from vendor content, so upgrades do not overwrite them.
- Check that package metrics match agreed internal definitions, or you will end up with two versions of key numbers.
- Confirm where the package runs and stores data, and whether it uses your governance, security and semantic layer or its own.

# Questions to ask

- Which business processes run on standard commercial applications with little customisation?
- How quickly are results needed, compared with building from scratch?
- Who will own vendor upgrades and local extensions?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Governed metric definitions](metric-definitions.md), [Planning and forecasting](enterprise-planning.md), [SaaS application connectors](../ingestion-integration/saas-connectors.md), [Semantic layer](semantic-layer.md), [Vendor-supplied application data products](../data-products/application-data-products.md) |

# Where it appears

- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Fusion Data Intelligence](../../technologies/oracle/oracle-fusion-data-intelligence.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud](../../technologies/sap/sap-business-data-cloud.md) |
