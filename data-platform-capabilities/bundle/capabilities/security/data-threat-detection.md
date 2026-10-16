---
type: Capability
id: data-threat-detection
title: Data threat detection
description: Analyse data access behaviour to detect and respond to insider threats, ransomware and abnormal access.
aliases: [insider risk, database activity monitoring, database firewall]
broader: [security]
related:
- audit-logging
- data-security-posture
- immutable-backups
- data-anomaly-detection
- data-loss-prevention
depends_on: [audit-logging]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data threat detection analyses audit and access logs to spot behaviour that suggests an attack or misuse, then alerts or acts. It learns normal patterns for each user, service and dataset and flags departures from them: an account reading far more sensitive rows than usual, bulk exports just before an employee leaves, a service account touching tables it has never used, or mass deletes and overwrites that look like ransomware. Database activity monitoring and database firewalls apply similar rules in line, blocking suspicious statements before they run.

Credentials get stolen and insiders misuse access, so access control alone does not prevent breaches; detection shortens the time before someone notices. Responses range from alerting a security operations team to automatic containment, such as suspending a session or revoking a token. Posture management finds what could go wrong; data loss prevention inspects content leaving specific routes.

# Key considerations

- Detection is only as good as the logs. Fix shared service accounts and missing read logs first.
- Send platform audit logs, with classification context, to the monitoring system the security team already uses rather than running a separate console.
- Agree automatic responses in advance, such as suspending a user or locking a table, and test that they do not disrupt important pipelines.
- Watch for destructive patterns, such as dropped tables, shortened retention or deleted backups, which often come before ransomware demands.

# Questions to ask

- Who would notice today if an account started exporting large volumes of customer data?
- Are platform audit logs sent to a security monitoring system, and with what context?
- Which automatic responses would the business accept?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Related | [Audit logging](audit-logging.md), [Data anomaly detection](../data-quality/data-anomaly-detection.md), [Data breach response](data-breach-response.md), [Data loss prevention](data-loss-prevention.md), [Data security posture management](data-security-posture.md), [Immutable backups](../platform-operations/immutable-backups.md), [Observability data analytics](../specialised-data/observability-analytics.md) |
| Depends on | [Audit logging](audit-logging.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 4, Measured)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 10 – Detection; Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23); Chapter VI – Information-sharing arrangements (Article 45) · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality; Articles 33 and 34 – Personal data breach notification

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Insider Risk Management](../../technologies/microsoft/purview-insider-risk-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Security Command Center](../../technologies/google-cloud/gcp-security-command-center.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Trust Center](../../technologies/snowflake/snowflake-trust-center.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Data Safe](../../technologies/oracle/oracle-data-safe.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Guardium Data Security Center](../../technologies/ibm/ibm-guardium-data-security-center.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Varonis Data Security Platform](../../technologies/independent/varonis-data-security-platform.md) |
