---
type: Capability
id: data-products
title: Data products
description: Manage data as products with owners, consumers, contracts and service levels.
aliases: [data mesh enablement, data product management]
broader: []
related: [data-domains, data-marketplace, data-observability, internal-data-sharing, data-certification]
depends_on: [data-catalogue, data-ownership]
order: 17
tags: [data-products]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data product is a dataset, or a small set of related outputs, that is built and run for identified consumers in the way a software product is. It has a named owner, a documented purpose, a stable interface such as tables, views, an API or a stream, published quality and service levels, and a version history. A customer orders product from the sales domain is something other teams can depend on, not a table they happen to find.

The capabilities in this domain make that promise explicit and enforceable. A specification describes the product in machine-readable form. Contracts fix the schema, meaning and quality consumers can rely on, and service levels set targets for freshness and availability. Lifecycle management handles versions, deprecation and retirement with notice. Vendor-supplied application data products extend the idea to datasets that software vendors maintain.

Data products are central to data mesh, where domains own and publish them, but the idea works for central teams too. They rely on cataloguing, sharing, quality monitoring and access control; the product layer adds accountability on top.

# Key considerations

- Not every table is a product. Keep the label for outputs with real consumers, and keep working tables private.
- Ownership must be funded. A product without a team that answers to its consumers is just a dataset with a label.
- Separate the product's public interface from its internal implementation, so producers can refactor without breaking consumers.
- Measure products by consumer use and incident rates, not by how many are published.

# Questions to ask

- Which datasets do several teams depend on today, and who answers when they break?
- Are domains expected to own and publish their own data, or will a central team?
- How do consumers learn about changes to datasets they depend on?
- Is there an agreed way to describe and register a data product?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Data contracts](data-contracts.md), [Data product lifecycle management](data-product-lifecycle.md), [Data product specification](data-product-specification.md), [Data product usage metering](data-product-metering.md), [Data service levels](data-slas.md), [Vendor-supplied application data products](application-data-products.md) |
| Related | [Metadata and discovery](../metadata/metadata.md), [Governance and compliance](../governance/governance.md), [Data sharing and collaboration](../data-sharing/data-sharing.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Data certification](../metadata/data-certification.md), [Data domains](../governance/data-domains.md), [Data marketplace](../data-sharing/data-marketplace.md), [Data observability](../data-quality/data-observability.md), [Internal data sharing](../data-sharing/internal-data-sharing.md) |
| Depends on | [Data catalogue](../metadata/data-catalogue.md), [Ownership and stewardship](../governance/data-ownership.md) |

# Where it appears

- **Maturity tracks:** [Data products](../../maturity/track-data-products.md)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | Knowledge Catalog data products |  |
| [SAP](../../platforms/platform-sap.md) | Data products (BDC) |  |

Narrower capabilities are realised by a further 24 technologies; see their pages.
