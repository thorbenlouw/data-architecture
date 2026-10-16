---
type: Use Case
id: usecase-data-monetisation
title: Data sharing and monetisation
description: Share or sell data products to partners and customers under agreed terms.
aliases: [data commercialisation, data as a product for partners]
requires:
- {capability: external-data-sharing, level: 3, why: 'Consumers get live, governed access instead of uncontrolled file copies.'}
- {capability: data-product-specification, level: 3, why: 'Each product needs a documented purpose, contents, owner and terms that buyers can read.'}
- {capability: data-contracts, level: 3, why: 'Schema, meaning and quality are promised to paying consumers and must be enforced.'}
- {capability: data-slas, level: 3, why: Freshness and availability are part of the commercial agreement and must be measured.}
- {capability: data-usage-rights, level: 3, why: Licence terms for owned and third-party data must allow the sharing and be checked against it.}
- {capability: consent-management, level: 3, why: Personal data can be shared only where consent or another lawful basis covers the purpose.}
- {capability: deidentification, level: 3, why: Most products must be aggregated or deidentified so individuals cannot be identified.}
- {capability: row-level-security, level: 3, why: Each consumer sees only the slice of data their contract covers.}
- {capability: audit-logging, level: 3, why: 'Consumer access is recorded for billing, contract compliance and audit.'}
- {capability: data-quality-rules, level: 3, why: Quality problems in a paid product become contract disputes.}
- {capability: data-product-lifecycle, level: 2, why: Versions and deprecations must be announced to consumers with notice.}
benefits_from:
- {capability: data-marketplace, why: Lets buyers find and subscribe to products.}
- {capability: data-clean-rooms, why: Allows joint analysis with partners without either side seeing the other's raw data.}
- {capability: open-protocol-sharing, why: Reaches consumers who use other platforms.}
- {capability: cross-region-sharing, why: Serves consumers in other clouds and regions.}
- {capability: privacy-enhancing-technologies, why: Adds formal privacy protection such as differential privacy to aggregates.}
- {capability: application-sharing, why: Ships analysis code with the data so consumers can run it in their own environment.}
- {capability: system-telemetry, why: Provides usage figures for usage-based pricing.}
- {capability: data-residency, why: Supports consumers whose data must stay in a given jurisdiction.}
personas:
- persona-data-product-owner
- persona-cdo
- persona-security-officer
- persona-risk-compliance
- persona-data-engineer
- persona-data-steward
patterns: [data-mesh]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Organisations hold data that partners, suppliers and customers value: point-of-sale data for suppliers, aggregated payment trends, logistics events, benchmarks. Sharing or selling it creates revenue or strengthens relationships, but only when legal permission, privacy, licence terms and service levels are handled properly. Data products are defined with a contract, deidentified or aggregated where needed, and shared live with each consumer under their entitlements, with usage tracked for billing and audit.

Good looks like products that consumers can find, understand and rely on, delivered to agreed service levels, with access that can be granted or revoked in minutes, clear evidence that each use is permitted by consent and licence, and revenue that covers the cost of running the product.

# Non-functional requirements

- Delivery service levels are written into contracts, for example daily by 06:00 with 99.5 per cent availability.
- Re-identification risk is assessed and documented for every product containing data derived from individuals.
- Access can be revoked immediately when a contract ends.
- Consumer usage is logged for billing and audit.

# Risks

- Third-party data is resold in breach of its licence, or personal data is shared without a lawful basis.
- Products shared as file exports leave the organisation's control.
- Products are not maintained after launch and consumers leave.
- Revenue does not cover the cost of serving, supporting and governing the product.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [External data sharing](../capabilities/data-sharing/external-data-sharing.md) | [Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md) | 3 (Defined) | Consumers get live, governed access instead of uncontrolled file copies. |
| [Data product specification](../capabilities/data-products/data-product-specification.md) | [Data products](../capabilities/data-products/data-products.md) | 3 (Defined) | Each product needs a documented purpose, contents, owner and terms that buyers can read. |
| [Data contracts](../capabilities/data-products/data-contracts.md) | [Data products](../capabilities/data-products/data-products.md) | 3 (Defined) | Schema, meaning and quality are promised to paying consumers and must be enforced. |
| [Data service levels](../capabilities/data-products/data-slas.md) | [Data products](../capabilities/data-products/data-products.md) | 3 (Defined) | Freshness and availability are part of the commercial agreement and must be measured. |
| [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Licence terms for owned and third-party data must allow the sharing and be checked against it. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Personal data can be shared only where consent or another lawful basis covers the purpose. |
| [De-identification](../capabilities/governance/deidentification.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Most products must be aggregated or deidentified so individuals cannot be identified. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Each consumer sees only the slice of data their contract covers. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Consumer access is recorded for billing, contract compliance and audit. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Quality problems in a paid product become contract disputes. |
| [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) | [Data products](../capabilities/data-products/data-products.md) | 2 (Managed) | Versions and deprecations must be announced to consumers with notice. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Data marketplace](../capabilities/data-sharing/data-marketplace.md) | Lets buyers find and subscribe to products. |
| [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md) | Allows joint analysis with partners without either side seeing the other's raw data. |
| [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md) | Reaches consumers who use other platforms. |
| [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md) | Serves consumers in other clouds and regions. |
| [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md) | Adds formal privacy protection such as differential privacy to aggregates. |
| [Data application distribution](../capabilities/data-sharing/application-sharing.md) | Ships analysis code with the data so consumers can run it in their own environment. |
| [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md) | Provides usage figures for usage-based pricing. |
| [Data residency and sovereignty](../capabilities/governance/data-residency.md) | Supports consumers whose data must stay in a given jurisdiction. |

# Personas

- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.
- [Chief data officer](../personas/persona-cdo.md): Accountable for the organisation's data strategy, value, risk and governance.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.
- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.

# Patterns

- [Data mesh](../patterns/data-mesh.md)

# Frameworks that apply

- [EU Data Act](../frameworks/framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.
- [Open Data Contract Standard (ODCS)](../frameworks/framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.
- [Open Data Product Standard (ODPS)](../frameworks/framework-bitol-odps.md): An open YAML standard for describing a data product, its input and output ports, management interfaces, team and support.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 6 of 11 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 7 of 11 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 8 of 11 | [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 7 of 11 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Databricks](../platforms/platform-databricks.md) | 5 of 11 | [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 2 of 11 | [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [De-identification](../capabilities/governance/deidentification.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [Informatica](../platforms/platform-informatica.md) | 5 of 11 | [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 3 of 11 | [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [De-identification](../capabilities/governance/deidentification.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [Oracle](../platforms/platform-oracle.md) | 4 of 11 | [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [SAP](../platforms/platform-sap.md) | 5 of 11 | [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [De-identification](../capabilities/governance/deidentification.md), [Audit logging](../capabilities/security/audit-logging.md) |
| [Teradata](../platforms/platform-teradata.md) | 2 of 11 | [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [De-identification](../capabilities/governance/deidentification.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [IBM](../platforms/platform-ibm.md) | 5 of 11 | [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Row-level security](../capabilities/security/row-level-security.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
| [Palantir](../platforms/platform-palantir.md) | 5 of 11 (+1 in preview) | [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Data service levels](../capabilities/data-products/data-slas.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md) (preview only) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 9 of 11 | [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Independent vendors](../platforms/platform-independent.md) | 9 of 11 | [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data product lifecycle management](../capabilities/data-products/data-product-lifecycle.md) |
