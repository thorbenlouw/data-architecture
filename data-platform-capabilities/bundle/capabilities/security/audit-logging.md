---
type: Capability
id: audit-logging
title: Audit logging
description: Record who accessed or changed what, when and from where, and keep the records tamper-evident.
aliases: [access history, audit trail]
broader: [security]
related: [compliance-evidence, data-threat-detection, system-telemetry, usage-metadata, immutable-backups]
depends_on: [identity-authentication]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Audit logs record security-relevant actions with who, what, when, where and how: sign-ins, queries and the tables and columns they touched, permission changes, policy edits, exports, shares and administrative actions. For example, an entry shows that a named analyst, connecting through a BI tool from the corporate network, read the `customer_contact` table at 14:02 and exported 20,000 rows. Logs are delivered to protected storage outside the reach of the people being audited and made tamper-evident through write-once storage, hash chaining or signing.

Audit logs are the evidence behind investigations, breach notifications, access reviews and audits, and the input to threat detection and usage analysis. Gaps are common: tools that connect through a shared service account log the account, not the person; some engines log statements but not which columns were read; services use different formats and clocks. Retention should match investigation and regulatory needs, which can be years in regulated sectors. Platform observability differs: it records performance and failures for operations, not actions for accountability.

# Key considerations

- Check that logs name the end user, not only a service account, for queries made through BI tools, applications and agents.
- Log reads as well as changes for sensitive data, at table and preferably column level.
- Send logs to a separate account or store with restricted delete rights, so administrators cannot erase their own trail.
- Bring logs from all platform services into one queryable form with consistent identities and timestamps.
- Logs can contain personal data, such as literal values in query text. Apply access control and retention to them too.

# Questions to ask

- What would an investigator need to reconstruct who accessed a given record last month?
- Do logs cover reads, exports and permission changes across every engine and tool?
- How long must audit logs be kept, and who may delete them?
- Are logs sent to a security monitoring system today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Related | [ML operations](../mlops/mlops.md), [Data sharing and collaboration](../data-sharing/data-sharing.md), [Access control](access-control.md), [Agent identity and authorisation](../generative-ai/agent-identity.md), [Agent tool and data access](../generative-ai/agent-tool-access.md), [Approved manual adjustments](../analytics-bi/manual-adjustments.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Data entry and write-back](../analytics-bi/data-writeback.md), [Data threat detection](data-threat-detection.md), [External data sharing](../data-sharing/external-data-sharing.md), [Human oversight of AI](../governance/human-oversight.md), [Identity and authentication](identity-authentication.md), [Immutable backups](../platform-operations/immutable-backups.md), [Inference logging](../mlops/inference-logging.md), [Managed file transfer](../ingestion-integration/managed-file-transfer.md), [Platform observability](../platform-operations/platform-observability.md), [Privileged access management](privileged-access.md), [SQL and programmatic access](../serving/sql-access.md), [Storage credential vending](../storage/credential-vending.md), [Usage and popularity metadata](../metadata/usage-metadata.md), [Usage and system telemetry](../platform-operations/system-telemetry.md) |
| Depends on | [Identity and authentication](identity-authentication.md) |
| Needed by | [Compliance controls and evidence](../governance/compliance-evidence.md), [Data breach response](data-breach-response.md), [Data threat detection](data-threat-detection.md), [Privileged access management](privileged-access.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (requires, level 3) · [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 3) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (benefits from) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [Risk and compliance officer](../../personas/persona-risk-compliance.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 12 – Review · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 12 Data Retention, Archiving and Purging (Data lifecycle) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Security · [DCAM v3](../../frameworks/framework-edm-dcam.md): 7 Data Management Operations, Risk & Control · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 10 – Detection; Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23) · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 12 – Record-keeping; Articles 19 and 26(6) – Log retention · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality; Article 5(2) – Accountability; Article 32 – Security of processing; Articles 33 and 34 – Personal data breach notification

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS CloudTrail data events | [AWS CloudTrail](../../technologies/aws/aws-cloudtrail.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Audit](../../technologies/microsoft/purview-audit.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Logging](../../technologies/google-cloud/gcp-cloud-logging.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Access History](../../technologies/snowflake/snowflake-access-history.md), [Snowflake Trust Center](../../technologies/snowflake/snowflake-trust-center.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks system tables](../../technologies/databricks/databricks-system-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Query Insights and system tables](../../technologies/clickhouse/clickhouse-cloud-monitoring.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [IDMC Administrator](../../technologies/informatica/informatica-administrator.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Shared Data Experience (SDX)](../../technologies/cloudera/cloudera-sdx.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Data Safe](../../technologies/oracle/oracle-data-safe.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database security (roles, row-level security, encryption)](../../technologies/teradata/teradata-security.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Guardium Data Security Center](../../technologies/ibm/ibm-guardium-data-security-center.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry security controls](../../technologies/palantir/palantir-security-controls.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Viya security controls](../../technologies/sas/sas-viya-security.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku DSS](../../technologies/dataiku/dataiku.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Ranger](../../technologies/open-source/apache-ranger.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Privacera](../../technologies/independent/privacera.md), [Varonis Data Security Platform](../../technologies/independent/varonis-data-security-platform.md) |
