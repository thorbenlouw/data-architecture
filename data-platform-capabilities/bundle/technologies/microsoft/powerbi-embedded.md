---
type: Technology
id: powerbi-embedded
title: Power BI Embedded
description: Embeds Power BI reports and dashboards in custom applications, either for an organisation's own users or for external customers without Power BI licences.
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [embedded-analytics, external-identity]
resource: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embedded-analytics-power-bi
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

App-owns-data embedding uses a service principal and an A, EM, P or F capacity. Some Power BI features behave differently or are unavailable when embedded, so check the embedding documentation for the features a product depends on.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) (Analytics and BI) (primary): Put dashboards and analytics inside other applications and portals, often for external customers.
- [External user and tenant identity](../../capabilities/security/external-identity.md) (Security and access): Manage identities, tenants and permissions for customers and partners who use data products or embedded analytics.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Power BI

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [External user and tenant identity](../../capabilities/security/external-identity.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md), [Conversational Analytics in Looker](../google-cloud/gcp-looker-conversational-analytics.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md), [External user and tenant identity](../../capabilities/security/external-identity.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Visualization](../cloudera/cloudera-data-visualization.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Analytics Cloud](../sap/sap-analytics-cloud.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Visual Analytics](../sas/sas-visual-analytics.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Sisense](../independent/sisense.md), [ThoughtSpot Analytics](../independent/thoughtspot-analytics.md), [Domo](../independent/domo.md) | [Embedded analytics](../../capabilities/analytics-bi/embedded-analytics.md) |
