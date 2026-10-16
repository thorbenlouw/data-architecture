---
type: Capability
id: internal-data-sharing
title: Internal data sharing
description: Share live data between teams, accounts and workspaces without copying it.
aliases: [zero-copy sharing]
broader: [data-sharing]
related: [catalogue-federation, multi-tenancy, data-domains, cost-attribution, data-contracts]
depends_on: [table-catalogue, access-control]
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A finance domain working in its own workspace or account publishes a set of curated tables. The marketing team, in a different workspace with its own compute and budget, sees them in its catalogue and queries them directly. The provider's storage holds the only copy, updates are visible straight away, and access is granted and revoked in one place.

This matters in organisations that split work across accounts, workspaces or regions for isolation, cost tracking or a domain-oriented model such as data mesh. Without it, teams copy data between environments with pipelines, adding cost, delay and conflicting versions. Mechanisms include cross-workspace grants in a shared catalogue, cross-account shares and federated catalogues. The consumer usually pays for its own queries, which keeps costs attributable. Internal sharing differs from external sharing mainly in trust, identity and contract: internal consumers use the same identity provider and policies.

# Key considerations

- Share stable, documented interfaces such as curated tables or views, not internal working tables, so producers can change their internals.
- Check that classifications, masking and row filters travel with the share and apply in the consumer's environment.
- Decide who pays for queries and storage, and make it visible in cost attribution.
- Track who consumes each share, so producers know whom a change will affect.

# Questions to ask

- How many workspaces, accounts or domains exist, and how do they exchange data today?
- Do pipelines copy the same data into several environments?
- Must consumer usage be charged back to the consuming team?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data sharing and collaboration](data-sharing.md) |
| Broader | [Data sharing and collaboration](data-sharing.md) |
| Related | [Data products](../data-products/data-products.md), [Catalogue federation](../storage/catalogue-federation.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Data contracts](../data-products/data-contracts.md), [Data domains](../governance/data-domains.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md) |
| Depends on | [Table catalogue](../storage/table-catalogue.md), [Access control](../security/access-control.md) |

# Where it appears

- **Use cases:** [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (benefits from)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Data product owner](../../personas/persona-data-product-owner.md)
- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md) (from level 2, Managed)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Domain-oriented decentralised data ownership and architecture

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift data sharing; Lake Formation cross-account grants | [Amazon Redshift data sharing](../../technologies/aws/aws-redshift-data-sharing.md), [AWS Lake Formation](../../technologies/aws/aws-lake-formation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | OneLake shortcuts | [OneLake shortcuts](../../technologies/microsoft/fabric-onelake-shortcuts.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery sharing](../../technologies/google-cloud/gcp-bigquery-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Secure Data Sharing and organisational listings | [Snowflake Internal Marketplace (organisational listings)](../../technologies/snowflake/snowflake-internal-marketplace.md), [Snowflake Secure Data Sharing](../../technologies/snowflake/snowflake-secure-data-sharing.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks OpenSharing](../../technologies/databricks/databricks-opensharing.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Marketplace (CDMP)](../../technologies/informatica/informatica-cloud-data-marketplace.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud](../../technologies/sap/sap-business-data-cloud.md), [SAP Business Warehouse in SAP Business Data Cloud](../../technologies/sap/sap-business-warehouse-bdc.md), [SAP Databricks](../../technologies/sap/sap-databricks.md) (distribution of Databricks), [SAP Snowflake](../../technologies/sap/sap-snowflake.md) (unconfirmed; distribution of Snowflake) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Fabric](../../technologies/teradata/teradata-fabric.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenSharing protocol](../../technologies/open-source/delta-sharing.md) |
