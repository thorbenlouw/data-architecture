---
type: Persona
id: persona-risk-compliance
title: Risk and compliance officer
description: Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
cares_about:
- compliance-evidence
- critical-data-elements
- cross-system-lineage
- data-reconciliation
- audit-logging
- data-quality-scorecards
- ai-governance
- model-governance
- data-retention
- records-of-processing
- resilience-testing
- ai-impact-assessment
- ai-incident-management
- data-residency
- governance-metrics
- data-issue-management
- data-ownership
- human-oversight
- temporal-data
- time-travel
- immutable-backups
patterns: [shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Risk and compliance officers sit in the second line of defence, with internal audit as the third. In financial services they oversee rules such as BCBS 239 and DORA; elsewhere they cover GDPR, the EU AI Act, sector regulation and financial reporting controls. They map obligations to controls, test that the controls work and report the results to committees and regulators.

They rarely use the platform directly. They ask for control descriptions, test results, lineage, reconciliations and logs, and judge success by clean audits, few repeat findings and fast, consistent answers to regulators.

# Goals

- Map every relevant regulatory obligation to platform controls with a named owner.
- Get evidence that controls are operating without collecting it by hand each time.
- Show regulators the lineage and quality of every figure in a submission.
- Keep AI systems inventoried, risk-classified and assessed.

# Jobs

- Maintain the control framework and map it to platform controls.
- Request and review evidence for audits and regulatory examinations.
- Review incidents, quality breaches and the progress of remediation.
- Check lineage and reconciliations for regulatory reports and critical data elements.
- Oversee AI risk classification, impact assessments and incident reporting.
- Review resilience test results against operational resilience rules.

# Pain points

- Evidence is spread across tools and gathered by hand in spreadsheets.
- Lineage stops at the warehouse, so figures cannot be traced to their source.
- Controls are documented but not tested.
- Ownership of new AI obligations is unclear.

# Questions they ask

- Can we trace every figure in this submission back to source, including each transformation?
- Which controls are automated and evidenced continuously, and which rely on people?
- How do we show that retention and deletion policies are actually applied?
- Which of our AI systems fall under high-risk rules, and what evidence do we hold for each?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) | [Governance and compliance](../capabilities/governance/governance.md) | Map regulatory requirements to platform controls and produce evidence for auditors. |
| [Critical data elements](../capabilities/governance/critical-data-elements.md) | [Governance and compliance](../capabilities/governance/governance.md) | Identify the data items that matter most for regulatory, risk and financial reporting and apply stricter controls to them. |
| [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Stitch lineage across ingestion tools, platforms and BI tools into one connected view. |
| [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Prove that data moved between systems is complete and correct using counts, totals and record matching. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | Record who accessed or changed what, when and from where, and keep the records tamper-evident. |
| [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Track quality results over time and report them by dataset, domain and quality dimension. |
| [AI governance](../capabilities/governance/ai-governance.md) | [Governance and compliance](../capabilities/governance/governance.md) | Inventory AI systems and govern their risk, approval, documentation and use in line with regulation. |
| [Model governance](../capabilities/mlops/model-governance.md) | [ML operations](../capabilities/mlops/mlops.md) | Keep an inventory of models with owners, approvals, documentation and risk ratings throughout their life. |
| [Retention and disposal](../capabilities/governance/data-retention.md) | [Governance and compliance](../capabilities/governance/governance.md) | Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed. |
| [Records of processing](../capabilities/governance/records-of-processing.md) | [Governance and compliance](../capabilities/governance/governance.md) | Keep a register of personal data processing with purposes, categories, recipients and retention, linked to the data involved. |
| [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Test backup, recovery and failover regularly and record the results as evidence. |
| [AI impact assessment](../capabilities/governance/ai-impact-assessment.md) | [Governance and compliance](../capabilities/governance/governance.md) | Assess and record an AI system's effects on people and society before release and whenever it changes. |
| [AI incident management](../capabilities/governance/ai-incident-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | Record, investigate and report incidents and malfunctions involving AI systems, including notifying regulators where required. |
| [Data residency and sovereignty](../capabilities/governance/data-residency.md) | [Governance and compliance](../capabilities/governance/governance.md) | Keep data and its processing in approved jurisdictions and prove that you have. |
| [Governance coverage metrics](../capabilities/governance/governance-metrics.md) | [Governance and compliance](../capabilities/governance/governance.md) | Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement. |
| [Data issue management](../capabilities/data-quality/data-issue-management.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Log, assign, track and resolve data quality incidents with their owners. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | Assign accountable owners and stewards to data and record their responsibilities. |
| [Human oversight of AI](../capabilities/governance/human-oversight.md) | [Governance and compliance](../capabilities/governance/governance.md) | Route model and agent decisions to people for review, approval or override, and let them pause or stop a system. |
| [Bitemporal data](../capabilities/specialised-data/temporal-data.md) | [Specialised data types](../capabilities/specialised-data/specialised-data.md) | Store and query data as it was true in the real world and as it was recorded in the system. |
| [Time travel](../capabilities/storage/time-travel.md) | [Storage and table management](../capabilities/storage/storage.md) | Query or restore a table as it was at an earlier point in time or version. |
| [Immutable backups](../capabilities/platform-operations/immutable-backups.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | Keep backups that nobody can delete or change before they expire, with legal holds, to protect against ransomware. |

# Patterns

- [Shift-left data quality and governance](../patterns/shift-left.md)

# Use cases they take part in

- [Agentic process automation](../use-cases/usecase-agentic-automation.md): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Credit decisioning](../use-cases/usecase-credit-decisioning.md): Score credit applications and decide to approve, decline or refer them, with reasons, fairness checks and model risk controls.
- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md): Share or sell data products to partners and customers under agreed terms.
- [Privacy rights handling](../use-cases/usecase-privacy-rights.md): Find, report and erase an individual's data across the estate within legal deadlines.
- [Real-time fraud detection](../use-cases/usecase-fraud-detection.md): Score transactions in milliseconds and block or flag suspicious ones.
- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md): Produce accurate, auditable and reproducible submissions to regulators.
- [Security and log analytics](../use-cases/usecase-security-log-analytics.md): Collect and analyse large volumes of logs to detect threats and investigate incidents.
- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.

# Frameworks they work with

- [BCBS 239](../frameworks/framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [CDMC (Cloud Data Management Capabilities)](../frameworks/framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [DCAM v3](../frameworks/framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.
- [DORA (Digital Operational Resilience Act)](../frameworks/framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.
- [EU AI Act](../frameworks/framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [EU Data Act](../frameworks/framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.
- [GDPR](../frameworks/framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.
- [ISO/IEC 42001:2023](../frameworks/framework-iso-iec-42001.md): The international standard for an AI management system, setting requirements for governing AI responsibly within an organisation.
- [NIST AI Risk Management Framework (AI RMF 1.0)](../frameworks/framework-nist-ai-rmf.md): A voluntary framework for managing AI risk through four functions, Govern, Map, Measure and Manage, broken into categories and subcategories of outcomes.
