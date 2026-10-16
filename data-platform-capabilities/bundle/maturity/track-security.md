---
type: Maturity Track
id: track-security
title: Security and access control
description: How well data is protected from unauthorised access, loss and misuse, from identity through fine-grained access to threat detection.
covers:
- security
- identity-authentication
- access-control
- role-based-access
- attribute-based-access
- row-level-security
- column-masking
- access-requests
- encryption
- customer-managed-keys
- cryptographic-agility
- network-security
- audit-logging
- secrets-management
- data-loss-prevention
- data-security-posture
- data-threat-detection
- compute-user-isolation
- credential-vending
- permission-aware-retrieval
- agent-identity
- deidentification
- privileged-access
related_tracks: [track-privacy, track-governance, track-platform-self-service, track-resilience]
levels:
- level: 1
  name: Initial
  summary: Access relies on shared credentials and one-off grants, with provider defaults for everything else.
  criteria:
  - People and jobs connect with shared or long-lived credentials, some embedded in code.
  - Access is granted per user per table on request and is rarely removed.
  - Encryption relies on the provider's defaults, and nobody has checked which data endpoints are reachable from the internet.
  capabilities: [encryption]
- level: 2
  name: Managed
  summary: Central identity, role-based grants, managed secrets and private networking are in place.
  criteria:
  - People sign in through single sign-on, and services use short-lived credentials or managed identities.
  - Permissions are granted to roles mapped to directory groups, not to individuals.
  - Pipeline credentials live in a secrets manager, and secret scanning of repositories finds none in code.
  - Platform endpoints are reachable only from private networks or allow-listed addresses.
  - Logs of sign-ins and data access are retained for a defined period.
  capabilities:
  - access-control
  - identity-authentication
  - role-based-access
  - secrets-management
  - network-security
  - audit-logging
- level: 3
  name: Defined
  summary: Fine-grained access is defined once from tags and attributes and enforced the same way in every engine, and privileged access is granted only when needed.
  criteria:
  - Access rules, row filters, column masks and tokenisation are defined once from tags on data and attributes of users and enforced identically in every engine, so a newly tagged sensitive column is protected without new grants.
  - Access requests go through a workflow in which owners approve, set an expiry and recertify access periodically.
  - Direct grants on storage buckets are limited to platform service identities that the catalogue uses to vend scoped credentials, and a scheduled check reports any person holding one.
  - Tests confirm that Python or Scala code on shared clusters cannot read tables or files its user has not been granted, and the tests rerun after each platform upgrade.
  - Administrator, emergency and vendor support access is granted only for a stated task, with approval and an expiry, and every privileged session is logged for review.
  capabilities:
  - attribute-based-access
  - row-level-security
  - column-masking
  - deidentification
  - access-requests
  - credential-vending
  - compute-user-isolation
  - privileged-access
- level: 4
  name: Measured
  summary: Exposure and behaviour are monitored continuously, keys are customer-controlled, and AI access is per user.
  criteria:
  - Scans continuously map where sensitive data is, who can reach it and which settings put it at risk, and findings are closed within target times.
  - Platform data is encrypted with customer-managed keys, and rotation and revocation have been tested.
  - Unusual access such as bulk downloads or access at odd hours raises alerts that the security team triages.
  - Sensitive data leaving approved boundaries through exports, shares or email is detected and blocked.
  - Penetration tests include attempts to make AI assistants and agents disclose data the test user cannot open, and failures are tracked as security findings.
  capabilities:
  - data-security-posture
  - customer-managed-keys
  - data-threat-detection
  - data-loss-prevention
  - permission-aware-retrieval
  - agent-identity
- level: 5
  name: Optimising
  summary: Permissions, detection and cryptography are tuned continuously from usage and incident evidence.
  criteria:
  - Permissions unused for a defined period are found from access logs and removed after owner confirmation.
  - An inventory of the cryptography protecting data exists, and a change of algorithm, such as to post-quantum ciphers, has been rehearsed without reworking data.
  - Detection rules are tuned from incident outcomes, and the false-positive rate is tracked.
  - Audit logs are tamper-evident and checked for completeness against platform activity.
  capabilities: [cryptographic-agility]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up replaces shared accounts and broad grants with central identity, least-privilege access down to rows and columns, keys the organisation controls, and continuous detection of risky configurations and behaviour. CDMC key controls 7 and 9 describe what regulated firms are expected to show for sensitive data, which corresponds to levels 3 and 4 here. Typical blockers are legacy service accounts nobody dares remove, role sprawl when every request creates a new role, and access rules written separately in every engine.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Access relies on shared credentials and one-off grants, with provider defaults for everything else.

- People and jobs connect with shared or long-lived credentials, some embedded in code.
- Access is granted per user per table on request and is rarely removed.
- Encryption relies on the provider's defaults, and nobody has checked which data endpoints are reachable from the internet.

**Capabilities first relied on:** [Encryption](../capabilities/security/encryption.md)

## Level 2: Managed

Central identity, role-based grants, managed secrets and private networking are in place.

- People sign in through single sign-on, and services use short-lived credentials or managed identities.
- Permissions are granted to roles mapped to directory groups, not to individuals.
- Pipeline credentials live in a secrets manager, and secret scanning of repositories finds none in code.
- Platform endpoints are reachable only from private networks or allow-listed addresses.
- Logs of sign-ins and data access are retained for a defined period.

**Capabilities first relied on:** [Access control](../capabilities/security/access-control.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Role-based access control](../capabilities/security/role-based-access.md), [Secrets management](../capabilities/security/secrets-management.md), [Network security](../capabilities/security/network-security.md), [Audit logging](../capabilities/security/audit-logging.md)

## Level 3: Defined

Fine-grained access is defined once from tags and attributes and enforced the same way in every engine, and privileged access is granted only when needed.

- Access rules, row filters, column masks and tokenisation are defined once from tags on data and attributes of users and enforced identically in every engine, so a newly tagged sensitive column is protected without new grants.
- Access requests go through a workflow in which owners approve, set an expiry and recertify access periodically.
- Direct grants on storage buckets are limited to platform service identities that the catalogue uses to vend scoped credentials, and a scheduled check reports any person holding one.
- Tests confirm that Python or Scala code on shared clusters cannot read tables or files its user has not been granted, and the tests rerun after each platform upgrade.
- Administrator, emergency and vendor support access is granted only for a stated task, with approval and an expiry, and every privileged session is logged for review.

**Capabilities first relied on:** [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Row-level security](../capabilities/security/row-level-security.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [De-identification](../capabilities/governance/deidentification.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [Privileged access management](../capabilities/security/privileged-access.md)

## Level 4: Measured

Exposure and behaviour are monitored continuously, keys are customer-controlled, and AI access is per user.

- Scans continuously map where sensitive data is, who can reach it and which settings put it at risk, and findings are closed within target times.
- Platform data is encrypted with customer-managed keys, and rotation and revocation have been tested.
- Unusual access such as bulk downloads or access at odd hours raises alerts that the security team triages.
- Sensitive data leaving approved boundaries through exports, shares or email is detected and blocked.
- Penetration tests include attempts to make AI assistants and agents disclose data the test user cannot open, and failures are tracked as security findings.

**Capabilities first relied on:** [Data security posture management](../capabilities/security/data-security-posture.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md)

## Level 5: Optimising

Permissions, detection and cryptography are tuned continuously from usage and incident evidence.

- Permissions unused for a defined period are found from access logs and removed after owner confirmation.
- An inventory of the cryptography protecting data exists, and a change of algorithm, such as to post-quantum ciphers, has been rehearsed without reworking data.
- Detection rules are tuned from incident outcomes, and the false-positive rate is tracked.
- Audit logs are tamper-evident and checked for completeness against platform activity.

**Capabilities first relied on:** [Cryptographic agility](../capabilities/security/cryptographic-agility.md)

# Capabilities in scope

[Security and access](../capabilities/security/security.md), [Access control](../capabilities/security/access-control.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Agent identity and authorisation](../capabilities/generative-ai/agent-identity.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Audit logging](../capabilities/security/audit-logging.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Cryptographic agility](../capabilities/security/cryptographic-agility.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [De-identification](../capabilities/governance/deidentification.md), [Encryption](../capabilities/security/encryption.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Permission-aware retrieval](../capabilities/generative-ai/permission-aware-retrieval.md), [Privileged access management](../capabilities/security/privileged-access.md), [Role-based access control](../capabilities/security/role-based-access.md), [Row-level security](../capabilities/security/row-level-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Shared compute isolation](../capabilities/security/compute-user-isolation.md), [Storage credential vending](../capabilities/storage/credential-vending.md)

# Related tracks

- [Privacy](track-privacy.md): How reliably the organisation meets its obligations to the people its data describes, from purpose and consent to rights requests and de-identification.
- [Governance operating model](track-governance.md): How clearly the rules, roles and controls for managing data are defined, implemented on the platform and evidenced.
- [Platform self-service](track-platform-self-service.md): How far teams can obtain, run and observe what they need on the shared platform without waiting for a central team.
- [Resilience and recovery](track-resilience.md): How well the platform withstands and recovers from data loss, corruption, ransomware and outages within agreed targets.

Levels follow the shared [maturity scale](maturity-scale.md).
