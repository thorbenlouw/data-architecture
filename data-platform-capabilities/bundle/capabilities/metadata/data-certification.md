---
type: Capability
id: data-certification
title: Data certification
description: Mark assets as trusted, deprecated or under review so consumers know what to rely on.
aliases: [endorsement, trust badges]
broader: [data-catalogue]
related: [data-quality-scorecards, data-contracts, data-product-lifecycle, usage-metadata]
depends_on: [data-ownership]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Certification is a status attached to an asset, such as certified, under review or deprecated, set by its owner or a steward against agreed criteria. Typical criteria are a named owner, documentation, passing quality checks and a defined refresh schedule. The status shows as a badge in the catalogue, BI tools and search results and can be used to rank or filter them. For example, two revenue tables exist; the certified one carries a badge in the BI tool, while the deprecated one warns users and names its replacement and retirement date.

It tells consumers which of many similar assets to rely on and gives owners a clear standard to meet. It only works when the criteria are explicit and checked; otherwise badges are applied loosely and stop meaning anything. Mature setups work out eligibility automatically from quality results and ownership, and remove certification when checks start failing. Data contracts define what a producer guarantees, and the published outputs of data products are usually the assets that get certified.

# Key considerations

- Write the criteria down and turn as many as possible into automatic checks.
- Withdraw or flag certification automatically when quality checks or freshness targets fail.
- Deprecation needs a replacement, a retirement date and notice to current users, found from usage and lineage.
- Show badges where people choose data, in BI and SQL tools, not only in the catalogue.

# Questions to ask

- Do users struggle to choose between similar datasets?
- Who may certify assets, and against which criteria?
- How are consumers told when a dataset is being deprecated?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data catalogue](data-catalogue.md) |
| Related | [Analytics and BI](../analytics-bi/analytics-bi.md), [Data products](../data-products/data-products.md), [Active metadata](active-metadata.md), [Dashboards and interactive reports](../analytics-bi/dashboards-reports.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data contracts](../data-products/data-contracts.md), [Data issue management](../data-quality/data-issue-management.md), [Data product lifecycle management](../data-products/data-product-lifecycle.md), [Data quality scorecards](../data-quality/data-quality-scorecards.md), [Data trust indicators](data-trust-indicators.md), [Governed metric definitions](../analytics-bi/metric-definitions.md), [Usage and popularity metadata](usage-metadata.md) |
| Depends on | [Ownership and stewardship](../governance/data-ownership.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 2) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2)
- **Patterns:** [Data marts](../../patterns/data-marts.md) · [Medallion architecture](../../patterns/medallion-architecture.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Business user](../../personas/persona-business-user.md) · [Chief data officer](../../personas/persona-cdo.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 3 – Accuracy and integrity · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 3 Authoritative Data Sources and Provisioning Points (Governance and accountability) · [DCAM v3](../../frameworks/framework-edm-dcam.md): 6 Govern Data & DMP · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Authoritative Definitions · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Authoritative Definitions

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Endorsement (promoted, certified, master data) | [OneLake catalog](../../technologies/microsoft/fabric-onelake-catalog.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Discover](../../technologies/databricks/databricks-discover.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Atlan](../../technologies/independent/atlan.md), [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md), [Tableau Cloud](../../technologies/independent/tableau-cloud.md) |
