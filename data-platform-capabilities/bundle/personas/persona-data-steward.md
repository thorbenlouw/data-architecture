---
type: Persona
id: persona-data-steward
title: Data steward
description: Looks after the definition, quality and proper use of data in a business domain.
cares_about:
- business-glossary
- data-catalogue
- stewardship-workflows
- data-quality-rules
- data-quality-scorecards
- data-issue-management
- data-classification
- data-ownership
- data-certification
- critical-data-elements
- access-requests
- reference-data-management
- data-profiling
- ai-generated-documentation
- data-trust-indicators
- metric-definitions
- active-metadata
- entity-resolution
- master-data-management
- survivorship
- data-domains
- data-lineage
- governance-metrics
patterns: [shift-left, data-mesh]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data stewards are usually business experts, such as a finance data lead or a customer data manager, for whom stewardship is part of the job rather than all of it. They answer to a data owner and work with the governance office and data engineers. Most of their time on the platform is spent in the catalogue, glossary, quality and access tools.

Success is data in their domain that is described, classified, owned and monitored, with quality issues fixed at source promptly and consumers clear about what each term means. Their influence depends on the tools making stewardship quick, because it competes with their other work.

# Goals

- Agree definitions of business terms and link them to the data that represents them.
- Keep the quality of critical data within agreed thresholds.
- Make sure sensitive data is classified correctly.
- Resolve data issues and access requests quickly.

# Jobs

- Write and approve glossary definitions and dataset descriptions.
- Define quality rules with data engineers and review scorecards.
- Triage data issues and follow them through to resolution with the owners.
- Review suggested classifications and approve tags.
- Approve or review access requests for domain data.
- Certify trusted datasets and deprecate obsolete ones.
- Maintain reference data and the matching rules used for master data.
- Confirm on a regular cycle that owners, descriptions and classifications in their domain are still correct.
- Review uncertain record matches and disputed merges in master data.

# Pain points

- Stewardship competes with the day job and is squeezed out.
- Catalogue entries are incomplete and go out of date.
- Consumers find quality problems before monitoring does.
- Departments use the same term to mean different things.
- Approval and review requests arrive by email and chat with no queue, deadline or record of the decision.

# Questions they ask

- Which data elements are critical and need the strictest controls?
- Can descriptions and classifications be suggested automatically for us to review?
- How do quality results reach the source system owners who can fix them?
- Where does my responsibility end and the data owner's or the engineer's begin?
- Can I see all my pending approvals in one place and act on them from the tools I already use?
- Do consumers see quality results and open issues where they use the data, or only in my scorecards?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Business glossary](../capabilities/metadata/business-glossary.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Define business terms and link them to the data that represents them. |
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Provide a searchable inventory of data assets with descriptions, owners, quality and usage. |
| [Stewardship workflows](../capabilities/governance/stewardship-workflows.md) | [Governance and compliance](../capabilities/governance/governance.md) | Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Define and run checks that data must pass, such as completeness, validity, uniqueness and consistency. |
| [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Track quality results over time and report them by dataset, domain and quality dimension. |
| [Data issue management](../capabilities/data-quality/data-issue-management.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Log, assign, track and resolve data quality incidents with their owners. |
| [Data classification](../capabilities/governance/data-classification.md) | [Governance and compliance](../capabilities/governance/governance.md) | Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | Assign accountable owners and stewards to data and record their responsibilities. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Mark assets as trusted, deprecated or under review so consumers know what to rely on. |
| [Critical data elements](../capabilities/governance/critical-data-elements.md) | [Governance and compliance](../capabilities/governance/governance.md) | Identify the data items that matter most for regulatory, risk and financial reporting and apply stricter controls to them. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle. |
| [Reference data management](../capabilities/master-data/reference-data-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | Manage shared code lists and mappings, such as country codes and product categories, with versions and approvals. |
| [Data profiling](../capabilities/data-quality/data-profiling.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Analyse data to understand its structure, distributions, completeness and anomalies. |
| [AI-generated documentation](../capabilities/metadata/ai-generated-documentation.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Draft descriptions, tags and documentation for data assets using AI, for people to review. |
| [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define, certify and version key business metrics with owners and calculation logic. |
| [Active metadata](../capabilities/metadata/active-metadata.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data. |
| [Entity resolution](../capabilities/master-data/entity-resolution.md) | [Master and reference data](../capabilities/master-data/master-data.md) | Find and link records that refer to the same real-world entity, even when they do not match exactly. |
| [Master data management](../capabilities/master-data/master-data-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | Create a single trusted record for entities such as customer, product or supplier from many sources. |
| [Merge and survivorship](../capabilities/master-data/survivorship.md) | [Master and reference data](../capabilities/master-data/master-data.md) | Combine matched records into a golden record using rules about which source wins for each attribute. |
| [Data domains](../capabilities/governance/data-domains.md) | [Governance and compliance](../capabilities/governance/governance.md) | Group data assets, products and owners into business domains with their own stewardship and policies. |
| [Data lineage](../capabilities/metadata/data-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Track where data comes from, how it is transformed and where it goes. |
| [Governance coverage metrics](../capabilities/governance/governance-metrics.md) | [Governance and compliance](../capabilities/governance/governance.md) | Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement. |

# Patterns

- [Shift-left data quality and governance](../patterns/shift-left.md)
- [Data mesh](../patterns/data-mesh.md)

# Use cases they take part in

- [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md): Business users ask questions of governed data in plain language and get trustworthy answers.
- [Customer 360](../use-cases/usecase-customer-360.md): Give every channel a single, trusted view of each customer.
- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md): Share or sell data products to partners and customers under agreed terms.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md): Produce trusted, consistent KPIs and management reports across the organisation.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md): A generative AI assistant that answers questions from internal documents, with citations.
- [Privacy rights handling](../use-cases/usecase-privacy-rights.md): Find, report and erase an individual's data across the estate within legal deadlines.
- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md): Produce accurate, auditable and reproducible submissions to regulators.
- [Self-service BI](../use-cases/usecase-self-service-bi.md): Analysts and business users explore governed data and build their own reports with trusted metrics.
- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.

# Frameworks they work with

- [BCBS 239](../frameworks/framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [DAMA-DMBOK 2](../frameworks/framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
- [DCAM v3](../frameworks/framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.
- [ISO 8000 (data quality)](../frameworks/framework-iso-8000.md): A series of international standards on data quality, covering concepts, quality management processes, profiling, rules, master data exchange and sensor data.
