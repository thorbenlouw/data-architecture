---
type: Capability
id: embedded-analytics
title: Embedded analytics
description: Put dashboards and analytics inside other applications and portals, often for external customers.
aliases: [customer-facing analytics, in-product analytics, white-label analytics, OEM analytics]
broader: [analytics-bi]
related: [real-time-analytics, external-data-sharing, data-apis, multi-tenancy, data-applications]
depends_on: [row-level-security, identity-authentication]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A customer portal that shows each client its own usage and spend, or a field sales app that shows account history, is usually built with embedded analytics. The host application signs the user in, then requests a signed, short-lived token from the analytics service that carries the user's identity and tenant. Content renders in a frame or through a component library, and every query is filtered to that tenant's rows.

It matters when analytics is part of a product or partner service rather than an internal tool. The hard parts are tenant isolation, performance for many concurrent external users, styling that matches the host application, and pricing that works for thousands of external viewers. Approaches range from embedding standard dashboards to building custom interfaces on analytics APIs. Embedded analytics differs from data sharing: the consumer sees results through an interface, never the data itself.

# Key considerations

- Tenant isolation is a security boundary. Enforce it in the data layer with row-level security tied to the token, not only in the front end.
- External users expect fast pages. Plan caching, pre-aggregation or a real-time serving store if queries must return in under a second.
- Check licence models. Per-user pricing designed for internal staff can become unaffordable for a large customer base.
- Decide whether customers may build their own reports or only view fixed ones, since self-service multiplies support and security work.

# Questions to ask

- Who will see the embedded content, how many of them, and are they inside or outside the organisation?
- How is each viewer's tenant identified, and where is that enforced?
- What response time does the host application need?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Data APIs](../serving/data-apis.md), [Data application hosting](../development-lifecycle/data-applications.md), [External data sharing](../data-sharing/external-data-sharing.md), [External user and tenant identity](../security/external-identity.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Real-time analytical database](../compute/real-time-analytics.md), [Result caching](../compute/result-caching.md), [Row-level security](../security/row-level-security.md) |
| Depends on | [Row-level security](../security/row-level-security.md), [Identity and authentication](../security/identity-authentication.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick Sight](../../technologies/aws/aws-quick-sight.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI Embedded](../../technologies/microsoft/powerbi-embedded.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Conversational Analytics in Looker](../../technologies/google-cloud/gcp-looker-conversational-analytics.md), [Looker](../../technologies/google-cloud/gcp-looker.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI/BI dashboards](../../technologies/databricks/databricks-ai-bi-dashboards.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Visualization](../../technologies/cloudera/cloudera-data-visualization.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Analytics Cloud](../../technologies/sap/sap-analytics-cloud.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Workshop](../../technologies/palantir/palantir-workshop.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Visual Analytics](../../technologies/sas/sas-visual-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Superset](../../technologies/open-source/apache-superset.md), [Metabase](../../technologies/open-source/metabase.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Domo](../../technologies/independent/domo.md), [Omni Analytics](../../technologies/independent/omni.md), [Sigma Computing](../../technologies/independent/sigma.md), [Sisense](../../technologies/independent/sisense.md), [Tableau Cloud](../../technologies/independent/tableau-cloud.md), [ThoughtSpot Analytics](../../technologies/independent/thoughtspot-analytics.md) |
