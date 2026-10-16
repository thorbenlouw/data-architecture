---
type: Capability
id: data-usage-rights
title: Data licensing and usage rights
description: Record licence terms and permitted uses of datasets and check use against them, including for model training.
aliases: [data rights management]
broader: [governance]
related: [consent-management, data-marketplace, model-lineage, external-data-sharing, attribute-based-access]
depends_on: [data-lineage]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Many datasets come with conditions: a licence from a data vendor, terms in a customer contract, an open-data licence or limits set by a partner. Usage rights management records those terms in structured form, such as permitted purposes, users, territories, duration, redistribution and derived use, attaches them to the datasets concerned and checks proposed uses against them. For example, market data licensed for internal display should not appear in a client report, and text acquired under some licences may not be used to train models.

The issue has grown with machine learning, because training is a use many older licences do not mention, and models outlive the data they learned from. Restrictions also travel: derived tables, features and models inherit them from their inputs, which needs lineage to trace. This differs from consent management, which deals with permissions individuals give about their personal data; usage rights concern contract and licence terms, which can apply to any data.

# Key considerations

- Translate licence terms into a small set of machine-readable permissions and restrictions that policies can check. Free-text contract summaries cannot be enforced.
- Propagate restrictions through lineage to derived tables, features and models, and record which datasets each model was trained on.
- Licence expiry should trigger action, such as removing access or deleting data, not only a reminder.
- Record terms when data is acquired, with procurement and legal, while the contract is to hand.

# Questions to ask

- Which third-party datasets are licensed, and where are the licence terms recorded?
- Are any datasets barred from model training or from use in external products?
- Can you list which models were trained on a given licensed dataset?
- What happens to derived data when a licence ends?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Data sharing and collaboration](../data-sharing/data-sharing.md), [Attribute- and tag-based access control](../security/attribute-based-access.md), [Consent and purpose management](consent-management.md), [Data clean rooms](../data-sharing/data-clean-rooms.md), [Data enrichment](../processing/data-enrichment.md), [Data marketplace](../data-sharing/data-marketplace.md), [External data sharing](../data-sharing/external-data-sharing.md), [Geospatial data](../specialised-data/geospatial-data.md), [Model customisation](../generative-ai/model-customisation.md), [Model lineage](../metadata/model-lineage.md), [Training and evaluation dataset management](../machine-learning/training-dataset-management.md), [Vendor-supplied application data products](../data-products/application-data-products.md) |
| Depends on | [Data lineage](../metadata/data-lineage.md) |

# Where it appears

- **Use cases:** [Credit decisioning](../../use-cases/usecase-credit-decisioning.md) (requires, level 2) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 8 Data Consumption Purpose (Accessibility and usage) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Handling Ethics · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 53 – Obligations of general-purpose AI model providers · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapters II and III – Access to and sharing of connected-product data; Chapter IV – Unfair contractual terms; Chapter VIII – Interoperability · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.7 – Data for AI systems · [NIST AI Risk Management Framework (AI RMF 1.0)](../../frameworks/framework-nist-ai-rmf.md): GOVERN 6 – Third-party risk; MAP 4 – Risks of components

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Marketplace (CDMP)](../../technologies/informatica/informatica-cloud-data-marketplace.md) |
