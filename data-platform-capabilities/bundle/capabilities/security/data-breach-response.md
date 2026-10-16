---
type: Capability
id: data-breach-response
title: Data breach response
description: Work out which data and which people a security incident exposed, assess the risk, and notify regulators and affected individuals within legal deadlines, keeping a record of each decision.
aliases: [breach notification, breach impact assessment, data incident response, breach investigation]
broader: [security, privacy-management]
related:
- data-threat-detection
- data-security-posture
- entity-resolution
- platform-incident-management
- ai-incident-management
depends_on: [audit-logging, data-classification]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When credentials are stolen, a bucket is found open or an export goes to the wrong recipient, privacy and security teams must establish quickly which records were exposed, whose data they hold and how harmful the exposure is. Audit logs show what was read or copied, classification shows which of it was personal or sensitive, and entity resolution turns rows into a list of affected people and their countries. A case record holds the timeline, the risk assessment, each decision on whether to notify and the notices sent.

The GDPR requires notice to the supervisory authority within 72 hours of becoming aware of a breach that poses a risk, and other laws and sector rules set their own deadlines, so the speed of scoping often decides whether a deadline is met. Approaches range from privacy tools with breach case management, through security tools that analyse a compromised identity's access, to prepared audit-log queries. Threat detection spots the incident; platform incident management restores service rather than assessing harm to people.

# Key considerations

- Scoping is only as good as the logs. Check that reads are logged with the end user and the tables or columns touched, and kept long enough to cover late discovery.
- Prepare queries and runbooks in advance, such as everything one identity read in a period, so the first hours are not spent writing them.
- Map data subjects to jurisdictions before an incident. Notification rules and deadlines differ by country and sector.
- Restrict access to the case record and keep it apart from the exposed data, because it will itself contain personal data.

# Questions to ask

- How long would it take today to list the people affected if one analyst account were misused for a week?
- Which regulators and sector rules apply, and what deadlines and thresholds do they set?
- Who decides whether to notify, and how is that decision recorded?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md), [Privacy management](../governance/privacy-management.md) |
| Related | [AI incident management](../governance/ai-incident-management.md), [Data security posture management](data-security-posture.md), [Data threat detection](data-threat-detection.md), [Entity resolution](../master-data/entity-resolution.md), [Platform incident management](../platform-operations/platform-incident-management.md) |
| Depends on | [Audit logging](audit-logging.md), [Data classification](../governance/data-classification.md) |

# Where it appears

- **Use cases:** [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 3, Defined)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23) · [GDPR](../../frameworks/framework-gdpr.md): Articles 33 and 34 – Personal data breach notification

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [BigID Next](../../technologies/independent/bigid-next.md), [OneTrust Privacy Automation](../../technologies/independent/onetrust-privacy-automation.md), [Securiti DataAI Command Platform](../../technologies/independent/securiti-dataai-command-platform.md), [Varonis Data Security Platform](../../technologies/independent/varonis-data-security-platform.md) |
