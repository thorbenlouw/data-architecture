---
type: Capability
id: security
title: Security and access
description: Protect data from unauthorised access, loss and misuse.
broader: []
related: [governance, data-classification, platform-observability, business-continuity, multi-tenancy]
order: 15
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Security stops data being read, changed or destroyed by people and systems that should not, and lets the organisation reconstruct what happened when something goes wrong. Data platforms pose particular problems: large amounts of sensitive data in one place, many users running their own code, many integration paths in and out, and access that must be controlled down to rows and columns.

The capabilities form layers. Identity and authentication establish who is acting, whether a person, a service or an agent. Access control decides what they may do, from role grants to row filters and column masks, with access requests to grant and review it. Encryption, network security and secrets management protect data and credentials at rest, in transit and inside pipelines. Shared compute isolation stops one user's code from bypassing controls on shared clusters. Audit logging records activity, and data loss prevention, posture management and threat detection use that record and the platform's configuration to find exposure and misuse.

Security depends on governance to know what is sensitive and what the rules are, and governance depends on security to enforce them. The main design choices are where enforcement happens (in each engine, in a shared catalogue or at the storage layer), how identity flows from the user through tools and agents to the data, and how far you trust the platform operator, which decides whether you need customer-managed keys and private networking.

# Key considerations

- Enforce access in a layer every engine passes through, such as the catalogue or storage credential issuing, so a new tool does not open a path around the controls.
- Carry the end user's identity through BI tools, applications and agents to the data. Shared service accounts hide who saw what and give everyone the same access.
- Prefer short-lived, automatically issued credentials to long-lived keys and passwords everywhere.
- Assume some control will fail. Combine prevention with logging, detection and tested recovery, including from ransomware.
- Map each managed service's shared-responsibility split and check the parts that fall to you.

# Questions to ask

- Which data on the platform would cause most harm if exposed, changed or destroyed?
- How does identity flow from users through tools and applications to queries?
- Which regulatory or customer requirements apply to encryption, keys, networking and audit?
- How quickly could you detect and contain a compromised account?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Access control](access-control.md), [AI supply chain security](ai-supply-chain-security.md), [Audit logging](audit-logging.md), [Data breach response](data-breach-response.md), [Data loss prevention](data-loss-prevention.md), [Data security posture management](data-security-posture.md), [Data threat detection](data-threat-detection.md), [De-identification](../governance/deidentification.md), [Encryption](encryption.md), [Identity and authentication](identity-authentication.md), [Network security](network-security.md), [Secrets management](secrets-management.md), [Shared compute isolation](compute-user-isolation.md) |
| Related | [Governance and compliance](../governance/governance.md), [Platform operations](../platform-operations/platform-operations.md), [Backup and disaster recovery](../platform-operations/business-continuity.md), [Data classification](../governance/data-classification.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Platform observability](../platform-operations/platform-observability.md) |

# Where it appears

- **Maturity tracks:** [Security and access control](../../maturity/track-security.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 148 technologies; see their pages.
