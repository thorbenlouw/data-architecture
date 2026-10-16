---
type: Persona
id: persona-security-officer
title: Security and privacy officer
description: Protects data and makes sure it is used lawfully.
cares_about:
- data-classification
- access-control
- data-policy-management
- audit-logging
- data-security-posture
- attribute-based-access
- column-masking
- row-level-security
- identity-authentication
- access-requests
- privileged-access
- encryption
- deidentification
- privacy-management
- data-subject-requests
- consent-management
- records-of-processing
- privacy-impact-assessment
- data-breach-response
- data-loss-prevention
- data-threat-detection
- data-retention
- crypto-shredding
- customer-managed-keys
- network-security
- permission-aware-retrieval
- agent-identity
- ai-guardrails
patterns: [shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In larger organisations this is two roles that work closely together: a security lead reporting to the chief information security officer, and a data protection officer or privacy lead. On the data platform they set requirements for identity, access, encryption, network controls, monitoring and the handling of personal data, review designs and new uses of data, and respond to incidents and individuals' requests.

Success is knowing where sensitive and personal data is and who can reach it, being able to show that access is least-privilege and logged, and handling breaches and privacy requests within legal deadlines. AI assistants and agents have added a new question to every review: what could this system reveal, or do, on someone's behalf?

# Goals

- Know where sensitive and personal data is, and who can access it.
- Enforce least-privilege access consistently across every engine and tool.
- Detect misuse and breaches quickly and respond within legal deadlines.
- Meet privacy obligations on lawful basis, minimisation, retention and individuals' rights.

# Jobs

- Set access control, encryption and network standards for the platform.
- Review classification results and scans for sensitive data.
- Run periodic access reviews and recertification.
- Monitor audit logs and threat alerts, and investigate incidents.
- Handle data subject requests and breach notifications.
- Review privacy impact assessments and approve new uses of personal data.
- Assess AI assistants and agents for data leakage and misuse risk.
- Investigate suspected breaches, establish which data and people were affected, and decide on notification.
- Approve and review privileged and emergency administrator access to the platform.

# Pain points

- Copies of personal data spread into sandboxes, exports and notebooks.
- Each tool defines permissions differently, so policies are applied inconsistently.
- Audit logs are incomplete or hard to query.
- AI tools may send sensitive data to external model providers.
- Erasure is hard to apply across backups, logs and derived tables.
- After an incident, nobody can say quickly which records and individuals were exposed.
- Administrators and service accounts hold permanent, broad rights that nobody reviews.

# Questions they ask

- Where is personal and sensitive data, and how is its classification kept current?
- Can we enforce one access policy across every engine and BI tool?
- How do we stop assistants and agents exposing data a user should not see?
- How do we handle erasure in backups, logs and model training data?
- Which encryption keys do we control, and what happens if we revoke them?
- If an analyst account was misused last week, can we list exactly which personal records it read?
- Who holds standing administrator rights, and can the provider's staff reach our data?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Data classification](../capabilities/governance/data-classification.md) | [Governance and compliance](../capabilities/governance/governance.md) | Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically. |
| [Access control](../capabilities/security/access-control.md) | [Security and access](../capabilities/security/security.md) | Decide who can see and change which data, at every level from account down to individual values. |
| [Policy management](../capabilities/governance/data-policy-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | Define data policies centrally and apply them consistently across platforms and tools. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | Record who accessed or changed what, when and from where, and keep the records tamper-evident. |
| [Data security posture management](../capabilities/security/data-security-posture.md) | [Security and access](../capabilities/security/security.md) | Find continuously where sensitive data lives, who can reach it and which configurations put it at risk. |
| [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) | [Security and access](../capabilities/security/security.md) | Grant or deny access based on attributes of the user and tags on the data. |
| [Column security and dynamic masking](../capabilities/security/column-masking.md) | [Security and access](../capabilities/security/security.md) | Hide or mask sensitive columns depending on who is querying. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | Restrict which rows each user sees based on who they are. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | Authenticate people and services through central identity, single sign-on and short-lived credentials. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle. |
| [Privileged access management](../capabilities/security/privileged-access.md) | [Security and access](../capabilities/security/security.md) | Grant administrator, emergency and vendor support access to the platform only when needed, with approval, time limits and a record of what was done. |
| [Encryption](../capabilities/security/encryption.md) | [Security and access](../capabilities/security/security.md) | Encrypt data at rest and in transit, with keys managed securely. |
| [De-identification](../capabilities/governance/deidentification.md) | [Governance and compliance](../capabilities/governance/governance.md) | Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk. |
| [Privacy management](../capabilities/governance/privacy-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | Meet privacy obligations such as purpose limitation, consent and individuals' rights over their data. |
| [Data subject requests](../capabilities/governance/data-subject-requests.md) | [Governance and compliance](../capabilities/governance/governance.md) | Find, export or erase a person's data across the platform when they ask. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | Record what each person agreed to and restrict use of their data to permitted purposes. |
| [Records of processing](../capabilities/governance/records-of-processing.md) | [Governance and compliance](../capabilities/governance/governance.md) | Keep a register of personal data processing with purposes, categories, recipients and retention, linked to the data involved. |
| [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md) | [Governance and compliance](../capabilities/governance/governance.md) | Trigger, carry out and record data protection impact assessments for high-risk processing, linked to the data and pipelines concerned. |
| [Data breach response](../capabilities/security/data-breach-response.md) | [Security and access](../capabilities/security/security.md) | Work out which data and which people a security incident exposed, assess the risk, and notify regulators and affected individuals within legal deadlines, keeping a record of each decision. |
| [Data loss prevention](../capabilities/security/data-loss-prevention.md) | [Security and access](../capabilities/security/security.md) | Detect and block sensitive data leaving approved boundaries. |
| [Data threat detection](../capabilities/security/data-threat-detection.md) | [Security and access](../capabilities/security/security.md) | Analyse data access behaviour to detect and respond to insider threats, ransomware and abnormal access. |
| [Retention and disposal](../capabilities/governance/data-retention.md) | [Governance and compliance](../capabilities/governance/governance.md) | Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed. |
| [Crypto-shredding](../capabilities/security/crypto-shredding.md) | [Security and access](../capabilities/security/security.md) | Make specific data unreadable everywhere, including in backups, by destroying the encryption keys that protect it. |
| [Customer-managed keys](../capabilities/security/customer-managed-keys.md) | [Security and access](../capabilities/security/security.md) | Encrypt platform data with keys you control, so you can rotate or revoke them. |
| [Network security](../capabilities/security/network-security.md) | [Security and access](../capabilities/security/security.md) | Keep data traffic on private networks and restrict where the platform can be reached from. |
| [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Filter retrieved content by each user's permissions in the source systems so AI answers never reveal what the user could not open. |
| [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time. |
| [AI guardrails](../capabilities/generative-ai/ai-guardrails.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions. |

# Patterns

- [Shift-left data quality and governance](../patterns/shift-left.md)

# Use cases they take part in

- [Agentic process automation](../use-cases/usecase-agentic-automation.md): AI agents complete multi-step business tasks using enterprise data and tools under controls.
- [Customer 360](../use-cases/usecase-customer-360.md): Give every channel a single, trusted view of each customer.
- [Customer-facing analytics](../use-cases/usecase-customer-facing-analytics.md): Give external customers fast, secure analytics inside a product.
- [Data sharing and monetisation](../use-cases/usecase-data-monetisation.md): Share or sell data products to partners and customers under agreed terms.
- [Knowledge assistant](../use-cases/usecase-rag-assistant.md): A generative AI assistant that answers questions from internal documents, with citations.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Marketing audience activation](../use-cases/usecase-marketing-activation.md): Build audiences from platform data and sync them to marketing and advertising tools.
- [Privacy rights handling](../use-cases/usecase-privacy-rights.md): Find, report and erase an individual's data across the estate within legal deadlines.
- [Security and log analytics](../use-cases/usecase-security-log-analytics.md): Collect and analyse large volumes of logs to detect threats and investigate incidents.
- [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md): Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.

# Frameworks they work with

- [CDMC (Cloud Data Management Capabilities)](../frameworks/framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [DORA (Digital Operational Resilience Act)](../frameworks/framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.
- [GDPR](../frameworks/framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.
