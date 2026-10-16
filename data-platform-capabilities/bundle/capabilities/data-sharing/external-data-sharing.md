---
type: Capability
id: external-data-sharing
title: External data sharing
description: Share live data with customers, partners and suppliers under agreed terms.
aliases: [secure data sharing, open sharing protocol]
broader: [data-sharing]
related: [data-usage-rights, deidentification, row-level-security, audit-logging, managed-file-transfer]
depends_on: [access-control]
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A retailer shares daily store sales with its suppliers, each seeing only its own products; a data provider shares a reference dataset with paying customers. In both cases the provider defines a share containing selected tables or views, adds the recipient, and can change or revoke it at any time. Recipients without an account on the same platform can be given a managed reader account, paid for by the provider.

It replaces file exports and partner pipelines, which go stale and leave copies outside your control. The harder questions are legal and commercial rather than technical: agreements on permitted use, personal data and liability; filtering so each recipient sees only what it is entitled to; auditing what was accessed; and who pays for compute. Sharing can stay within one platform and region, cross regions and clouds, or reach other platforms through open protocols.

# Key considerations

- Share through secure views or filtered tables, so recipients cannot infer anything about other recipients' data.
- Recipients' queries are visible to you. Agree in the contract what monitoring you do, and keep audit records.
- Personal data shared externally needs a legal basis and an agreement, and often de-identification first.
- Plan for revocation and offboarding, including what happens to data the recipient has already copied out.

# Questions to ask

- Which partners receive data from you today, how, and how often?
- Are recipients on the same platform, a different one, or none?
- What contract terms and permitted uses apply to each share?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data sharing and collaboration](data-sharing.md) |
| Broader | [Data sharing and collaboration](data-sharing.md) |
| Narrower | [Cross-region and cross-cloud sharing](cross-region-sharing.md), [Open-protocol sharing](open-protocol-sharing.md), [Vendor-supplied application data products](../data-products/application-data-products.md) |
| Related | [Audit logging](../security/audit-logging.md), [Data APIs](../serving/data-apis.md), [Data export](../serving/data-export.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Data loss prevention](../security/data-loss-prevention.md), [Data product usage metering](../data-products/data-product-metering.md), [De-identification](../governance/deidentification.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [External user and tenant identity](../security/external-identity.md), [Managed file transfer](../ingestion-integration/managed-file-transfer.md), [Privacy-enhancing technologies](../governance/privacy-enhancing-technologies.md), [Row-level security](../security/row-level-security.md), [Storage credential vending](../storage/credential-vending.md) |
| Depends on | [Access control](../security/access-control.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (benefits from)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data product owner](../../personas/persona-data-product-owner.md)
- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md) (from level 2, Managed)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter VI – Information-sharing arrangements (Article 45) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapters II and III – Access to and sharing of connected-product data; Chapter IV – Unfair contractual terms; Chapter V – Business-to-government access in exceptional need · [GDPR](../../frameworks/framework-gdpr.md): Article 19 – Notification to recipients · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Pricing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Clean Rooms](../../technologies/aws/aws-clean-rooms.md), [AWS Data Exchange](../../technologies/aws/aws-data-exchange.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Share](../../technologies/microsoft/azure-data-share.md), [External data sharing in Microsoft Fabric](../../technologies/microsoft/fabric-external-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery sharing (formerly Analytics Hub) exchanges and listings | [BigQuery sharing](../../technologies/google-cloud/gcp-bigquery-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../../technologies/snowflake/snowflake-listings.md), [Snowflake Native App Framework](../../technologies/snowflake/snowflake-native-app-framework.md), [Snowflake Open Data Sharing](../../technologies/snowflake/snowflake-open-data-sharing.md) (preview), [Snowflake Secure Data Sharing](../../technologies/snowflake/snowflake-secure-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) | OpenSharing | [Databricks OpenSharing](../../technologies/databricks/databricks-opensharing.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Syndigo MDM](../../technologies/independent/syndigo-mdm.md) |

Narrower capabilities are realised by a further 14 technologies; see their pages.
