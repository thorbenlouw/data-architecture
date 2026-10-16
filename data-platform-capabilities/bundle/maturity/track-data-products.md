---
type: Maturity Track
id: track-data-products
title: Data products
description: How far data is managed as products with accountable owners, known consumers, explicit contracts and service levels.
covers:
- data-products
- data-product-specification
- data-contracts
- data-slas
- data-product-lifecycle
- application-data-products
- data-product-metering
related_tracks: [track-data-quality, track-data-sharing, track-serving, track-finops]
levels:
- level: 1
  name: Initial
  summary: Datasets are built for single projects and reused informally.
  criteria:
  - Other teams reuse project datasets without the builders knowing.
  - Changes to shared tables are announced, if at all, after they have broken something.
  - Nobody can say which datasets have consumers outside the team that built them.
  capabilities: []
- level: 2
  name: Managed
  summary: A few shared datasets have owners, known consumers and advance notice of changes.
  criteria:
  - A small number of shared datasets have a named owner and a written purpose.
  - Consumers of those datasets are known, and breaking changes are announced to them in advance.
  - Expected refresh times for those datasets are written down.
  - Datasets published by business application vendors are used in place of custom extracts where they exist.
  capabilities: [application-data-products]
- level: 3
  name: Defined
  summary: Every product has a machine-readable specification and contracts checked in the producer's pipeline.
  criteria:
  - Each data product has a machine-readable specification, for example in ODPS, stating purpose, owner, output ports and terms of use.
  - Each output port has a contract, for example in ODCS, covering schema, meaning, quality rules and service levels.
  - Contract checks run in the producer's CI, and a change that breaks a contract cannot deploy without a new major version.
  - Consumers request access to a product from its catalogue entry and are recorded as consumers, so the owner always has a current consumer list.
  capabilities: [data-product-specification, data-contracts, data-slas]
- level: 4
  name: Measured
  summary: Service levels, versions and usage are measured and visible to producers and consumers.
  criteria:
  - Freshness, availability and quality are measured against each product's service levels, and breaches are visible to consumers.
  - Products are versioned, and deprecation notices with dates go automatically to every registered consumer.
  - Each product's use is metered per consumer, and consumer counts, usage and open issues are reported to its owner.
  capabilities: [data-product-lifecycle, data-product-metering]
- level: 5
  name: Optimising
  summary: The product portfolio is shaped by measured demand, cost and service-level history.
  criteria:
  - Products with no consumers or a high cost per consumer are retired through the standard lifecycle.
  - New products are proposed from demand data, such as frequent access requests or joins repeated by many consumers.
  - Service levels are revised from their history, for example tightening freshness where consumers need it and it has been met consistently.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means consumers pick datasets that carry a published contract, a named owner and measured service levels, and producers know who depends on them before they change anything. It applies the data-as-a-product principle of data mesh, and from level 3 products and contracts are described in machine-readable form such as Bitol's ODPS and ODCS. Typical blockers are relabelling tables as products without changing ownership, contracts written but never checked, and no funding for product owners.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Datasets are built for single projects and reused informally.

- Other teams reuse project datasets without the builders knowing.
- Changes to shared tables are announced, if at all, after they have broken something.
- Nobody can say which datasets have consumers outside the team that built them.

## Level 2: Managed

A few shared datasets have owners, known consumers and advance notice of changes.

- A small number of shared datasets have a named owner and a written purpose.
- Consumers of those datasets are known, and breaking changes are announced to them in advance.
- Expected refresh times for those datasets are written down.
- Datasets published by business application vendors are used in place of custom extracts where they exist.

**Capabilities first relied on:** [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md)

## Level 3: Defined

Every product has a machine-readable specification and contracts checked in the producer's pipeline.

- Each data product has a machine-readable specification, for example in ODPS, stating purpose, owner, output ports and terms of use.
- Each output port has a contract, for example in ODCS, covering schema, meaning, quality rules and service levels.
- Contract checks run in the producer's CI, and a change that breaks a contract cannot deploy without a new major version.
- Consumers request access to a product from its catalogue entry and are recorded as consumers, so the owner always has a current consumer list.

**Capabilities first relied on:** [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md)

## Level 4: Measured

Service levels, versions and usage are measured and visible to producers and consumers.

- Freshness, availability and quality are measured against each product's service levels, and breaches are visible to consumers.
- Products are versioned, and deprecation notices with dates go automatically to every registered consumer.
- Each product's use is metered per consumer, and consumer counts, usage and open issues are reported to its owner.

**Capabilities first relied on:** [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md)

## Level 5: Optimising

The product portfolio is shaped by measured demand, cost and service-level history.

- Products with no consumers or a high cost per consumer are retired through the standard lifecycle.
- New products are proposed from demand data, such as frequent access requests or joins repeated by many consumers.
- Service levels are revised from their history, for example tightening freshness where consumers need it and it has been met consistently.

# Capabilities in scope

[Data products](../capabilities/data-products/data-products.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md), [Data service levels](../capabilities/data-products/data-slas.md), [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md)

# Related tracks

- [Data quality and observability](track-data-quality.md): How systematically the organisation defines, measures, monitors and fixes the fitness of data for its intended uses.
- [Data sharing](track-data-sharing.md): How safely and efficiently data is shared between teams and with external parties without unnecessary copies.
- [Data serving](track-serving.md): How well curated data reaches applications, people and operational tools at the latency, volume and reliability they need.
- [FinOps](track-finops.md): How well the organisation understands, allocates and controls what the data platform costs, relative to the value it delivers.

Levels follow the shared [maturity scale](maturity-scale.md).
