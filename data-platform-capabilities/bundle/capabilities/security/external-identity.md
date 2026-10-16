---
type: Capability
id: external-identity
title: External user and tenant identity
description: Manage identities, tenants and permissions for customers and partners who use data products or embedded analytics.
aliases: [customer identity, CIAM]
broader: [identity-authentication]
related: [embedded-analytics, row-level-security, external-data-sharing, data-apis, data-product-metering]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

External users do not work for the organisation: customers viewing dashboards in a portal, suppliers reading their own sales figures, or partners calling a data API. They are usually held in a separate customer identity directory, or sign in through their own company's identity provider using SAML or OpenID Connect, and are grouped into tenants, typically one per customer organisation. Each request carries the user and tenant, which the platform uses to filter rows, choose which content appears and apply the customer's plan.

It matters for embedded analytics, data products sold to customers and partner portals. Scale and turnover differ from staff identity: thousands of organisations, each with its own administrators inviting and removing users, and no HR system to say who has left. A common pattern passes a short-lived signed token from the host application to the analytics service; another provisions users through SCIM. Putting external users in the staff directory often leads to over-shared access.

# Key considerations

- Enforce tenant isolation in the data layer, through row-level security or separate schemas per tenant, not only in the application. One missing filter can show one customer another's data.
- Let each customer's administrator invite, remove and review their own users where possible, with the platform enforcing limits.
- Decide whether tenants are rows in shared tables, separate schemas or separate databases. The choice affects isolation, cost and how easily one customer's data can be exported or deleted.
- Tokens passed to embedded content should be short-lived and carry only the attributes needed. Long-lived shared keys in a portal get copied and misused.
- Include external users in licence planning. Per-user pricing designed for staff can make customer-facing analytics expensive.

# Questions to ask

- How many external organisations and users are expected, and how fast will that grow?
- Do customers want to sign in with their own identity provider?
- Who adds and removes users at each customer, and how are leavers detected?
- What would it cost the organisation if one customer saw another's data?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Identity and authentication](identity-authentication.md) |
| Related | [Data APIs](../serving/data-apis.md), [Data product usage metering](../data-products/data-product-metering.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [External data sharing](../data-sharing/external-data-sharing.md), [Row-level security](row-level-security.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3)
- **Personas:** [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 4, Measured)
- **Frameworks:** [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapters II and III – Access to and sharing of connected-product data

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick Sight](../../technologies/aws/aws-quick-sight.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Entra ID](../../technologies/microsoft/azure-entra-id.md), [Power BI Embedded](../../technologies/microsoft/powerbi-embedded.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Looker](../../technologies/google-cloud/gcp-looker.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Keycloak](../../technologies/open-source/keycloak.md) |
