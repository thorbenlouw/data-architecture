---
type: Capability
id: data-marketplace
title: Data marketplace
description: Publish, find and subscribe to data products and datasets, internally or commercially.
aliases: [data exchange, listings]
broader: [data-sharing]
related:
- data-catalogue
- data-product-specification
- access-requests
- data-usage-rights
- data-consumer-portal
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A data marketplace is a storefront where providers list datasets or data products and consumers find, evaluate and subscribe to them. Each listing describes the data, its owner, update frequency, sample rows, terms of use and any price. When a consumer subscribes, the marketplace creates the underlying share or grant, often after an approval step, and records the subscription so the provider knows who uses what. Commercial marketplaces also handle billing; internal ones handle access requests.

Internal marketplaces suit organisations that run data as products across many domains and want consumers to serve themselves rather than ask around. External marketplaces let providers sell or distribute data, and let buyers acquire third-party data, such as weather or company records, without building ingestion. A marketplace overlaps with a catalogue but adds the transaction: listing, subscription, terms, approval and, for commercial data, payment and licence management.

# Key considerations

- Listings need product thinking: documentation, samples and service levels. Publishing raw tables gives a full shelf that nobody uses.
- Subscribing should create access automatically through platform sharing or grants, not raise a ticket for manual work.
- Record licence terms against each subscription and check use against them, especially for third-party data used in AI.
- Track subscribers and use per listing, so providers can prioritise, notify consumers of changes and retire unused products.

# Questions to ask

- Is the main goal internal discovery and reuse, distributing data to customers, or buying third-party data?
- How are access requests for shared data approved today, and how long do they take?
- Will any data be sold, and who handles pricing, billing and contracts?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data sharing and collaboration](data-sharing.md) |
| Broader | [Data sharing and collaboration](data-sharing.md) |
| Related | [Data products](../data-products/data-products.md), [Access requests and reviews](../security/access-requests.md), [Data application distribution](application-sharing.md), [Data catalogue](../metadata/data-catalogue.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data enrichment](../processing/data-enrichment.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Data product specification](../data-products/data-product-specification.md), [Data product usage metering](../data-products/data-product-metering.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from)
- **Personas:** [Data product owner](../../personas/persona-data-product-owner.md)
- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md) (from level 3, Defined)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – mesh supervision plane · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Pricing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS Data Exchange | [AWS Data Exchange](../../technologies/aws/aws-data-exchange.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Data products in Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-data-products.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery sharing with Google Cloud Marketplace | [BigQuery sharing](../../technologies/google-cloud/gcp-bigquery-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Snowflake Marketplace and Internal Marketplace | [Snowflake Cortex Knowledge Extensions](../../technologies/snowflake/snowflake-cortex-knowledge-extensions.md), [Snowflake Internal Marketplace (organisational listings)](../../technologies/snowflake/snowflake-internal-marketplace.md), [Snowflake Marketplace](../../technologies/snowflake/snowflake-marketplace.md), [Snowflake Native App Framework](../../technologies/snowflake/snowflake-native-app-framework.md) |
| [Databricks](../../platforms/platform-databricks.md) | Databricks Marketplace | [Databricks Marketplace](../../technologies/databricks/databricks-marketplace.md) |
| [Informatica](../../platforms/platform-informatica.md) | Cloud Data Marketplace data collections | [Informatica Cloud Data Marketplace (CDMP)](../../technologies/informatica/informatica-cloud-data-marketplace.md) |
| [SAP](../../platforms/platform-sap.md) | Data Marketplace (Datasphere) | [SAP Business Data Cloud data products](../../technologies/sap/sap-bdc-data-products.md), [SAP Datasphere catalog and Data Marketplace](../../technologies/sap/sap-datasphere-catalog.md) |
| [IBM](../../platforms/platform-ibm.md) | Data Product Hub | [IBM Data Product Hub](../../technologies/ibm/ibm-data-product-hub.md) |
| [Palantir](../../platforms/platform-palantir.md) | Marketplace | [Palantir DevOps and Marketplace](../../technologies/palantir/palantir-devops-marketplace.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md), [Denodo Platform](../../technologies/independent/denodo-platform.md) |
