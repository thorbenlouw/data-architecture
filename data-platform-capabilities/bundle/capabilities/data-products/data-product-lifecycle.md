---
type: Capability
id: data-product-lifecycle
title: Data product lifecycle management
description: Version, publish, deprecate and retire data products with notice to their consumers.
broader: [data-products]
related:
- data-contracts
- data-certification
- environment-promotion
- impact-analysis
- schema-change-management
depends_on: [usage-metadata]
tags: [data-products]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A product moves through stages such as proposed, in development, published, deprecated and retired. Changes are versioned: a compatible change such as adding a column is released in place, while a breaking change such as renaming a field is released as a new major version that runs in parallel with the old one. Consumers of the old version, found from query logs and subscriptions, are told the deprecation date and given migration notes.

It matters once products have consumers the producer does not talk to every day. Without it, producers either never change anything for fear of breaking someone, or change things and break them. Versions can be exposed through versioned table or view names, separate schemas or API versions. Retirement matters as much as release: unused products still cost money, carry security risk and clutter search. This differs from data versioning, which keeps past states of the data rather than versions of a product's interface.

# Key considerations

- Use semantic versioning or a similar convention so consumers can tell compatible changes from breaking ones.
- Running old and new versions in parallel costs compute and storage. Set a fixed overlap period.
- Identify consumers from actual query logs, not only registered subscriptions, before deprecating anything.
- Mark deprecated products in the catalogue and block new subscriptions, so the consumer list shrinks rather than grows.

# Questions to ask

- How are consumers told about changes to data they use today?
- How long must old versions be supported after a breaking change?
- How many published datasets have had no recent use?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data products](data-products.md) |
| Broader | [Data products](data-products.md) |
| Related | [Data certification](../metadata/data-certification.md), [Data contracts](data-contracts.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Impact analysis](../metadata/impact-analysis.md), [Privacy impact assessment](../governance/privacy-impact-assessment.md), [Schema change management](../development-lifecycle/schema-change-management.md) |
| Depends on | [Usage and popularity metadata](../metadata/usage-metadata.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 2)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Data product owner](../../personas/persona-data-product-owner.md)
- **Maturity tracks:** [Data products](../../maturity/track-data-products.md) (from level 4, Measured)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Data as a product; Self-serve platform – data product developer experience plane · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Fundamentals; Support & Communication Channels · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Fundamentals; Support and Communication Channels; Deprecated

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Data products in Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-data-products.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../../technologies/snowflake/snowflake-listings.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud data product studio](../../technologies/sap/sap-bdc-data-product-studio.md) (unconfirmed) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir DevOps and Marketplace](../../technologies/palantir/palantir-devops-marketplace.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Open Data Product Standard (ODPS)](../../technologies/open-source/open-data-product-standard.md) |
