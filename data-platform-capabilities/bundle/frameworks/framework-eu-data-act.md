---
type: Framework
id: framework-eu-data-act
title: EU Data Act
description: Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.
aliases: [Data Act, EU Data Act, Regulation (EU) 2023/2854]
kind: regulation
publisher: European Union
resource: https://digital-strategy.ec.europa.eu/en/policies/data-act
related: [framework-gdpr, framework-bitol-odcs]
applies_to:
- usecase-data-monetisation
- usecase-iot-predictive-maintenance
- usecase-platform-modernisation
- persona-data-product-owner
- persona-data-architect
- persona-risk-compliance
mappings:
- ref: Chapters II and III – Access to and sharing of connected-product data
  summary: Users can access data from connected products and related services and have it shared with third parties of their choice, who may use it only for the agreed purposes.
  capabilities: [data-apis, external-data-sharing, iot-ingestion, data-export, data-usage-rights, external-identity]
- ref: Chapter IV – Unfair contractual terms
  summary: Data-sharing terms imposed by a stronger party that are grossly unfair are not binding.
  capabilities: [data-contracts, data-usage-rights, external-data-sharing]
- ref: Chapter V – Business-to-government access in exceptional need
  summary: Public bodies can require privately held data for specific public-interest needs such as emergencies, with personal data limited and protected.
  capabilities: [external-data-sharing, data-export, deidentification, compliance-evidence]
- ref: Chapter VI – Switching between data processing services
  summary: Customers can move their data and workloads to another provider, with switching charges phased out.
  capabilities:
  - data-export
  - platform-migration
  - open-table-formats
  - file-formats
  - engine-interoperability
  - deployment-options
- ref: Chapter VII – Unlawful international governmental access
  summary: Cloud providers must take measures to prevent non-EU government access to non-personal data that conflicts with EU or national law.
  capabilities: [data-residency, customer-managed-keys, encryption, privileged-access]
- ref: Chapter VIII – Interoperability
  summary: Sets requirements for interoperable data spaces and data processing services, including machine-readable descriptions of datasets, licences, formats, code lists and access APIs.
  capabilities:
  - metadata-interoperability
  - data-product-specification
  - data-contracts
  - file-formats
  - data-apis
  - reference-data-management
  - data-usage-rights
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Data Act entered into force on 11 January 2024 and has applied since 12 September 2025. It gives users of connected products a right to access and share the data those products generate, bans unfair data-sharing terms between businesses, lets public bodies request data in exceptional need, and requires cloud and data processing providers to support switching and interoperability. Charges for switching providers must be abolished three years after entry into force, that is from January 2027. It matters to platform architects because it drives data export, open formats, interoperability and data-sharing capabilities, and the pending Digital Omnibus proposal would amend it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Chapters II and III – Access to and sharing of connected-product data | Users can access data from connected products and related services and have it shared with third parties of their choice, who may use it only for the agreed purposes. | [Data APIs](../capabilities/serving/data-apis.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Data export](../capabilities/serving/data-export.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [External user and tenant identity](../capabilities/security/external-identity.md) |
| Chapter IV – Unfair contractual terms | Data-sharing terms imposed by a stronger party that are grossly unfair are not binding. | [Data contracts](../capabilities/data-products/data-contracts.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md) |
| Chapter V – Business-to-government access in exceptional need | Public bodies can require privately held data for specific public-interest needs such as emergencies, with personal data limited and protected. | [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Data export](../capabilities/serving/data-export.md), [De-identification](../capabilities/governance/deidentification.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| Chapter VI – Switching between data processing services | Customers can move their data and workloads to another provider, with switching charges phased out. | [Data export](../capabilities/serving/data-export.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Open table formats](../capabilities/storage/open-table-formats.md), [Open file formats](../capabilities/storage/file-formats.md), [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md), [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md) |
| Chapter VII – Unlawful international governmental access | Cloud providers must take measures to prevent non-EU government access to non-personal data that conflicts with EU or national law. | [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Encryption](../capabilities/security/encryption.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| Chapter VIII – Interoperability | Sets requirements for interoperable data spaces and data processing services, including machine-readable descriptions of datasets, licences, formats, code lists and access APIs. | [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Data product specification](../capabilities/data-products/data-product-specification.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Open file formats](../capabilities/storage/file-formats.md), [Data APIs](../capabilities/serving/data-apis.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md) |

# Related frameworks

- [GDPR](framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.
- [Open Data Contract Standard (ODCS)](framework-bitol-odcs.md): An open YAML standard for describing a data contract, covering schema, quality, service levels, roles, pricing and where the data is served.

# Applies to

- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md) (use case): Share or sell data products to partners and customers under agreed terms.
- [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md) (use case): Analyse sensor telemetry to predict equipment failures before they happen.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md) (use case): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Data product owner](../personas/persona-data-product-owner.md) (persona): Owns the value, roadmap and consumers of one or more data products.
- [Data architect](../personas/persona-data-architect.md) (persona): Designs the data platform and how data flows, is modelled and is governed across the organisation.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
