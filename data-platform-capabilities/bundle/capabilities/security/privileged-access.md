---
type: Capability
id: privileged-access
title: Privileged access management
description: Grant administrator, emergency and vendor support access to the platform only when needed, with approval, time limits and a record of what was done.
aliases:
- PAM
- just-in-time access
- break-glass access
- privileged identity management
- operator access approval
broader: [access-control]
related: [identity-authentication, access-requests, secrets-management, audit-logging]
depends_on: [identity-authentication, audit-logging]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Administrator roles on a data platform can usually read every table, change policies and switch off audit settings, which makes them the accounts attackers want most. Privileged access management replaces standing administrator rights with elevation on request: an engineer who must change a network rule asks for the role for two hours, a second person approves, the elevation lapses automatically and the session is logged in detail. Emergency (break-glass) accounts are kept apart, protected by strong authentication, alarmed when used and reviewed afterwards. Some providers apply the same idea to their own staff, asking the customer to approve support access and logging it.

Least-privilege policies on data mean little if dozens of people hold permanent account-level administration. Auditors in financial services and the public sector expect privileged access to be time-limited, approved and reviewed, and data sovereignty concerns make operator access a common question in contract negotiations. The access request workflow manages ordinary data access for analysts and applications; secrets management stores the credentials that pipelines use.

# Key considerations

- Count the people and service accounts that hold administrator or owner roles on each platform and service before choosing tools.
- Make elevation fast for genuine incidents, or engineers keep standing rights in case they need them.
- Send privileged session records to a store that the elevated administrators cannot change or delete.
- Check whether the provider lets you approve and log its support staff's access, and what they can see without approval.

# Questions to ask

- How many people hold permanent administrator rights on the platform, and when were they last reviewed?
- How is emergency access obtained, and who reviews its use?
- Can the provider's staff reach your data, and would you know if they did?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Access control](access-control.md) |
| Related | [Access requests and reviews](access-requests.md), [Audit logging](audit-logging.md), [Identity and authentication](identity-authentication.md), [Secrets management](secrets-management.md) |
| Depends on | [Identity and authentication](identity-authentication.md), [Audit logging](audit-logging.md) |

# Where it appears

- **Use cases:** [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (benefits from)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 3, Defined)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 9 – Protection and prevention; Chapter V, Section I – ICT third-party risk management (Articles 28 to 30) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VII – Unlawful international governmental access

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Entra ID](../../technologies/microsoft/azure-entra-id.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Identity and Access Management](../../technologies/google-cloud/gcp-iam.md) |
