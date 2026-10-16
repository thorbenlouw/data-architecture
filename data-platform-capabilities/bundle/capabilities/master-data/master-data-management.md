---
type: Capability
id: master-data-management
title: Master data management
description: Create a single trusted record for entities such as customer, product or supplier from many sources.
aliases: [MDM, golden record]
broader: [master-data]
related: [data-quality-scorecards, reverse-etl, data-apis, data-issue-management]
depends_on: [data-cleansing, data-ownership]
tags: [master-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Records about customers, products, suppliers or other core entities are loaded from each source, cleaned and standardised, matched to find duplicates, and merged under survivorship rules into one golden record per entity. A cross-reference keeps every source identifier linked to the master identifier, so a customer known as C-1001 in billing and 88213 in the CRM resolves to one master customer. Data stewards review uncertain matches and correct records through workflows.

MDM supports accurate customer counts, single customer views, supplier spend analysis, regulatory reporting and consistent product data. Styles differ. A registry stores only links and match results; consolidation builds golden records for analytics; coexistence and centralised styles also send corrected data back to sources, or make the hub the place where records are created. MDM can cover one domain or several. Data cleansing fixes individual values, and entity resolution finds matches; MDM manages a governed record and its history over time.

# Key considerations

- Treat the source-to-master cross-reference as a primary output. Downstream systems need it to join data.
- Plan for splitting records apart. Wrong merges will happen, and undoing them must keep history.
- Decide the latency needed. Nightly batch suits analytics; customer onboarding may need matching at the moment of entry.
- Stewardship effort grows with the number of uncertain matches. Tune thresholds and staff the review queue.
- Track duplicate rates and master data quality over time to show the value delivered.

# Questions to ask

- Which entities and source systems come first?
- Must golden records flow back to operational systems, and how quickly?
- Who resolves uncertain matches and conflicting values, and how much time do they have?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Master and reference data](master-data.md) |
| Broader | [Master and reference data](master-data.md) |
| Narrower | [Entity resolution](entity-resolution.md), [Hierarchy management](hierarchy-management.md), [Merge and survivorship](survivorship.md) |
| Related | [Data quality and observability](../data-quality/data-quality.md), [Audience building and activation](../serving/audience-activation.md), [Data APIs](../serving/data-apis.md), [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Data domains](../governance/data-domains.md), [Data issue management](../data-quality/data-issue-management.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [Data quality scorecards](../data-quality/data-quality-scorecards.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Operational data store](../serving/operational-data-store.md), [Planning and forecasting](../analytics-bi/enterprise-planning.md), [Privacy management](../governance/privacy-management.md), [Reverse ETL](../serving/reverse-etl.md) |
| Depends on | [Data cleansing and standardisation](../data-quality/data-cleansing.md), [Ownership and stewardship](../governance/data-ownership.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from)
- **Patterns:** [Data Vault](../../patterns/data-vault.md) · [Dimensional modelling](../../patterns/dimensional-modelling.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Master and reference data](../../maturity/track-master-data.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 2 – Data architecture and IT infrastructure · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 3 Authoritative Data Sources and Provisioning Points (Governance and accountability) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Reference and Master Data · [Data mesh principles](../../frameworks/framework-data-mesh.md): Federated computational governance · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(d) – Accuracy; Article 16 – Right to rectification · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-100 and 8000-110 – Master data exchange and conformance to data specification; ISO 8000-115 to 8000-119 – Quality identifiers; ISO 8000-120 – Provenance

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) | MDM SaaS and 360 applications (Business 360) | [Informatica Customer 360 SaaS](../../technologies/informatica/informatica-customer-360.md), [Informatica Multidomain MDM SaaS](../../technologies/informatica/informatica-multidomain-mdm-saas.md), [Informatica Product 360 SaaS](../../technologies/informatica/informatica-product-360.md), [Informatica Supplier 360 SaaS](../../technologies/informatica/informatica-supplier-360.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Master Data Governance](../../technologies/sap/sap-master-data-governance.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Ataccama ONE Master Data Management](../../technologies/independent/ataccama-one-mdm.md), [K2view Data Product Platform](../../technologies/independent/k2view-data-product-platform.md), [Precisely EnterWorks](../../technologies/independent/precisely-enterworks.md), [Profisee MDM](../../technologies/independent/profisee-mdm.md), [Reltio Multidomain MDM](../../technologies/independent/reltio-multidomain-mdm.md), [Semarchy Data Platform](../../technologies/independent/semarchy-data-platform.md), [Stibo Systems STEP](../../technologies/independent/stibo-systems-step.md), [Syndigo MDM](../../technologies/independent/syndigo-mdm.md), [Tamr](../../technologies/independent/tamr.md) |

Narrower capabilities are realised by a further 19 technologies; see their pages.
