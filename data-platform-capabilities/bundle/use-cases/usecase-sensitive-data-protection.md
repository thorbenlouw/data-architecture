---
type: Use Case
id: usecase-sensitive-data-protection
title: Sensitive data protection
description: Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.
requires:
- capability: data-classification
  level: 4
  why: New tables and columns are scanned and labelled automatically as they land, because policies only protect what is tagged.
- {capability: metadata-harvesting, level: 3, why: 'New tables, files and extracts must be discovered automatically, or classification has gaps.'}
- {capability: attribute-based-access, level: 3, why: Policies attached to tags protect thousands of tables without a grant for each one.}
- {capability: data-policy-management, level: 3, why: One reviewed set of policies is pushed to every engine and tool instead of being rewritten in each.}
- {capability: column-masking, level: 3, why: Most users can work with sensitive tables if identifying fields are masked.}
- {capability: row-level-security, level: 2, why: 'Some datasets must be restricted by region, client or case assignment.'}
- {capability: deidentification, level: 2, why: Direct identifiers are tokenised or pseudonymised in analytical copies of the main personal datasets.}
- capability: identity-authentication
  level: 3
  why: BI tools, applications and agents pass the end user's identity, so policies and logs apply to the person, not a shared account.
- {capability: access-requests, level: 3, why: 'Access to restricted data is approved by owners, expires by default and is reviewed on a fixed cycle.'}
- {capability: data-ownership, level: 2, why: Each sensitive asset needs an owner who approves access and answers for its classification.}
- {capability: audit-logging, level: 3, why: 'Reads of restricted data are logged with the end user and the columns touched, for investigations and audits.'}
- {capability: data-security-posture, level: 3, why: Scans find copies outside the catalogue and work out who can effectively reach each sensitive store.}
- {capability: compliance-evidence, level: 3, why: 'Auditors ask for evidence that controls operated, drawn from platform records rather than screenshots.'}
benefits_from:
- {capability: active-metadata, why: Propagates sensitivity tags to derived tables through lineage.}
- {capability: column-lineage, why: Finds derived columns that carry sensitive values under other names.}
- {capability: data-loss-prevention, why: Blocks or flags bulk exports and shares of tagged data.}
- {capability: data-threat-detection, why: Alerts on unusual reads of sensitive data by people or services.}
- {capability: governance-metrics, why: Reports classification and policy coverage by domain against targets.}
- {capability: privileged-access, why: Removes standing administrator rights that bypass data policies.}
- {capability: credential-vending, why: Stops engines and people reading sensitive files directly from storage outside catalogue policy.}
- {capability: compute-user-isolation, why: Prevents code on shared clusters from bypassing row and column controls.}
- {capability: analytical-sandboxes, why: 'Keeps analysts'' working copies inside governed space, with expiry and the same policies.'}
- {capability: permission-aware-retrieval, why: Keeps AI assistants within the same permissions as other tools.}
- {capability: data-breach-response, why: Turns access logs and classification into a list of affected people quickly when something goes wrong.}
personas:
- persona-security-officer
- persona-data-steward
- persona-risk-compliance
- persona-platform-engineer
- persona-data-architect
- persona-data-engineer
patterns: [shift-left, data-fabric]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Large organisations hold customer, employee, payment and health data in hundreds of tables, files and extracts, read by several engines and BI tools. Regulators, auditors and control frameworks such as CDMC expect them to know where that data is, to grant access by policy rather than one request at a time, to mask or tokenise what most users do not need, and to show who read what. On the platform this means classifying data automatically as it lands, attaching masking and row policies to classification tags so they follow the data into every engine, granting access through approved and expiring requests, and scanning for copies and exposure the catalogue does not know about.

Good looks like every sensitive column labelled within a day of landing, protected by tag-based policies that give the same result in SQL, notebooks, BI and AI tools, access to restricted data reviewed on a fixed cycle with unused grants removed, and a security team that can say in minutes who could read a table and who did. Forgotten copies are found by scans, not by auditors.

# Non-functional requirements

- New tables and columns are scanned and classified within an agreed time of creation, often 24 hours.
- The same policy gives the same result in every engine and tool that reads the data, and this is retested after each platform upgrade.
- Access to restricted data expires by default, typically within 90 days, and existing access is recertified on a fixed cycle.
- Audit records of reads on restricted data name the end user and are kept for the regulatory period, often several years.
- Policy changes are reviewed and tested before they take effect.

# Risks

- Classification misses sensitive data in free text, files or derived tables, so policies never apply to it.
- Engines or tools that read storage directly bypass catalogue policies.
- A sensitive tag is removed or a policy changed without review, exposing a whole domain at once.
- Strict defaults block legitimate work, and people move data to unmanaged copies to get round them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Data classification](../capabilities/governance/data-classification.md) | [Governance and compliance](../capabilities/governance/governance.md) | 4 (Measured) | New tables and columns are scanned and labelled automatically as they land, because policies only protect what is tagged. |
| [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | New tables, files and extracts must be discovered automatically, or classification has gaps. |
| [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Policies attached to tags protect thousands of tables without a grant for each one. |
| [Policy management](../capabilities/governance/data-policy-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | One reviewed set of policies is pushed to every engine and tool instead of being rewritten in each. |
| [Column security and dynamic masking](../capabilities/security/column-masking.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Most users can work with sensitive tables if identifying fields are masked. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | 2 (Managed) | Some datasets must be restricted by region, client or case assignment. |
| [De-identification](../capabilities/governance/deidentification.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Direct identifiers are tokenised or pseudonymised in analytical copies of the main personal datasets. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | BI tools, applications and agents pass the end user's identity, so policies and logs apply to the person, not a shared account. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Access to restricted data is approved by owners, expires by default and is reviewed on a fixed cycle. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Each sensitive asset needs an owner who approves access and answers for its classification. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Reads of restricted data are logged with the end user and the columns touched, for investigations and audits. |
| [Data security posture management](../capabilities/security/data-security-posture.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Scans find copies outside the catalogue and work out who can effectively reach each sensitive store. |
| [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Auditors ask for evidence that controls operated, drawn from platform records rather than screenshots. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Active metadata](../capabilities/metadata/active-metadata.md) | Propagates sensitivity tags to derived tables through lineage. |
| [Column-level lineage](../capabilities/metadata/column-lineage.md) | Finds derived columns that carry sensitive values under other names. |
| [Data loss prevention](../capabilities/security/data-loss-prevention.md) | Blocks or flags bulk exports and shares of tagged data. |
| [Data threat detection](../capabilities/security/data-threat-detection.md) | Alerts on unusual reads of sensitive data by people or services. |
| [Governance coverage metrics](../capabilities/governance/governance-metrics.md) | Reports classification and policy coverage by domain against targets. |
| [Privileged access management](../capabilities/security/privileged-access.md) | Removes standing administrator rights that bypass data policies. |
| [Storage credential vending](../capabilities/storage/credential-vending.md) | Stops engines and people reading sensitive files directly from storage outside catalogue policy. |
| [Shared compute isolation](../capabilities/security/compute-user-isolation.md) | Prevents code on shared clusters from bypassing row and column controls. |
| [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md) | Keeps analysts' working copies inside governed space, with expiry and the same policies. |
| [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md) | Keeps AI assistants within the same permissions as other tools. |
| [Data breach response](../capabilities/security/data-breach-response.md) | Turns access logs and classification into a list of affected people quickly when something goes wrong. |

# Personas

- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.
- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Data architect](../personas/persona-data-architect.md): Designs the data platform and how data flows, is modelled and is governed across the organisation.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.

# Patterns

- [Shift-left data quality and governance](../patterns/shift-left.md)
- [Data fabric](../patterns/data-fabric.md)

# Frameworks that apply

- [CDMC (Cloud Data Management Capabilities)](../frameworks/framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [GDPR](../frameworks/framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 11 of 13 | [Policy management](../capabilities/governance/data-policy-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 11 of 13 | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Policy management](../capabilities/governance/data-policy-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 12 of 13 | [Policy management](../capabilities/governance/data-policy-management.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 12 of 13 | [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Databricks](../platforms/platform-databricks.md) | 11 of 13 | [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 4 of 13 | [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Policy management](../capabilities/governance/data-policy-management.md), [De-identification](../capabilities/governance/deidentification.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [Informatica](../platforms/platform-informatica.md) | 10 of 13 | [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 6 of 13 | [Policy management](../capabilities/governance/data-policy-management.md), [De-identification](../capabilities/governance/deidentification.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [Oracle](../platforms/platform-oracle.md) | 7 of 13 | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Policy management](../capabilities/governance/data-policy-management.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [SAP](../platforms/platform-sap.md) | 2 of 13 | [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Policy management](../capabilities/governance/data-policy-management.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [De-identification](../capabilities/governance/deidentification.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Audit logging](../capabilities/security/audit-logging.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [Teradata](../platforms/platform-teradata.md) | 2 of 13 | [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Policy management](../capabilities/governance/data-policy-management.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [De-identification](../capabilities/governance/deidentification.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [IBM](../platforms/platform-ibm.md) | 9 of 13 | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Row-level security](../capabilities/security/row-level-security.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md) |
| [Palantir](../platforms/platform-palantir.md) | 6 of 13 | [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Policy management](../capabilities/governance/data-policy-management.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [SAS](../platforms/platform-sas.md) | 6 of 13 | [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [De-identification](../capabilities/governance/deidentification.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 1 of 13 | [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Policy management](../capabilities/governance/data-policy-management.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Row-level security](../capabilities/security/row-level-security.md), [De-identification](../capabilities/governance/deidentification.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 10 of 13 | [Access requests and reviews](../capabilities/security/access-requests.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| [Independent vendors](../platforms/platform-independent.md) | 12 of 13 | [Identity and authentication](../capabilities/security/identity-authentication.md) |
