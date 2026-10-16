---
type: Capability
id: data-product-specification
title: Data product specification
description: Describe a data product's purpose, outputs, owners and terms of use in a standard, machine-readable form.
aliases: [data product descriptor]
broader: [data-products]
related:
- data-catalogue
- metadata-interoperability
- self-service-provisioning
- infrastructure-as-code
- data-marketplace
tags: [data-products]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In practice the specification is a YAML or JSON file kept with the product's code. It typically records name, domain, owner, purpose, output ports (the tables, views, APIs or topics consumers use), input dependencies, classifications, service levels, terms of use and links to contracts and documentation. CI validates the file, and publishing registers the product in the catalogue or marketplace.

A standard format lets a platform automate the work around a product: provisioning storage and access, catalogue registration, checking that required fields such as owner and classification are filled, and generating documentation. Several open specifications exist, such as the Open Data Product Specification and the Bitol project's Open Data Product Standard. A specification describes the whole product, while a data contract describes the guarantees on one output; a product may have several contracts.

# Key considerations

- Pick one specification and a small set of mandatory fields. Long templates get filled with placeholder text.
- Generate what you can, such as schema, lineage and usage, from the platform rather than asking owners to type it.
- Validate specifications in CI and block publishing when required fields such as owner or classification are missing.
- Check that your catalogue, marketplace and provisioning tools can read the chosen format.

# Questions to ask

- What must every data product declare before others may use it?
- Should publishing a specification trigger provisioning, catalogue registration or access set-up automatically?
- Which tools need to read product descriptions?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data products](data-products.md) |
| Broader | [Data products](data-products.md) |
| Related | [Data catalogue](../metadata/data-catalogue.md), [Data marketplace](../data-sharing/data-marketplace.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md), [Metadata interoperability](../metadata/metadata-interoperability.md), [Ownership and stewardship](../governance/data-ownership.md), [Self-service provisioning](../platform-operations/self-service-provisioning.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data architect](../../personas/persona-data-architect.md) · [Data product owner](../../personas/persona-data-product-owner.md)
- **Maturity tracks:** [Data products](../../maturity/track-data-products.md) (from level 3, Defined)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Data as a product · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VIII – Interoperability · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Fundamentals; Product Information (input and output ports); Context

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | SageMaker Catalog data products | [Amazon SageMaker Catalog](../../technologies/aws/aws-sagemaker-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Data products in Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-data-products.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data products](../../technologies/google-cloud/gcp-knowledge-catalog-data-products.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Internal Marketplace (organisational listings)](../../technologies/snowflake/snowflake-internal-marketplace.md), [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../../technologies/snowflake/snowflake-listings.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud data product studio](../../technologies/sap/sap-bdc-data-product-studio.md) (unconfirmed), [SAP Business Data Cloud data products](../../technologies/sap/sap-bdc-data-products.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Data Product Hub](../../technologies/ibm/ibm-data-product-hub.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Open Data Contract Standard (ODCS)](../../technologies/open-source/open-data-contract-standard.md), [Open Data Product Standard (ODPS)](../../technologies/open-source/open-data-product-standard.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Starburst Galaxy](../../technologies/independent/starburst-galaxy.md) |
