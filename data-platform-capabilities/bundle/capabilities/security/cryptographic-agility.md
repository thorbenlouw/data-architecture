---
type: Capability
id: cryptographic-agility
title: Cryptographic agility
description: Inventory the cryptography protecting data and change algorithms, for example to post-quantum ciphers, without rework.
aliases: [post-quantum readiness]
broader: [encryption]
related: [customer-managed-keys, secrets-management, network-security, compliance-evidence]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cryptographic agility means being able to change the cryptography that protects data without rebuilding systems. It starts with an inventory of where cryptography is used: TLS settings on endpoints and connectors, algorithms and key lengths for storage encryption, signing of tokens and artefacts, hashing in pseudonymisation, and the libraries that implement them. Systems then choose algorithms through configuration and policy rather than hard-coding them, and data can be re-encrypted under new algorithms and keys in place.

The main driver now is quantum computing. A large enough quantum computer would break widely used public-key algorithms such as RSA and elliptic-curve cryptography, which protect key exchange and signatures; symmetric ciphers such as AES-256 are considered much less affected. NIST published its first post-quantum standards in 2024, and several governments have set migration timelines. Data that must stay confidential for many years is already at risk, because traffic recorded today could be decrypted later ("harvest now, decrypt later"). Agility also helps whenever a specific algorithm or library is found to be weak.

# Key considerations

- Start with long-lived sensitive data and long-lived keys, such as archives and backups, which are most exposed to future decryption.
- Ask platform vendors for their post-quantum plans for TLS, key management and storage encryption, since much of the cryptography sits in services you do not control.
- Look for hard-coded algorithms in custom pipelines, clients and tokenisation code, which are often the slowest parts to change.
- Some financial regulation, including technical standards under DORA, expects firms to update cryptography as cryptanalysis advances. Keep the inventory current enough to show you can.

# Questions to ask

- Which data must stay confidential for ten years or more?
- Is there an inventory of algorithms, key lengths and libraries used across the platform and its integrations?
- Which components could switch algorithms through configuration, and which would need code changes?
- What do the platform's vendors plan for post-quantum support?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Encryption](encryption.md) |
| Related | [Compliance controls and evidence](../governance/compliance-evidence.md), [Customer-managed keys](customer-managed-keys.md), [Network security](network-security.md), [Secrets management](secrets-management.md) |

# Where it appears

- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Guardium Data Security Center](../../technologies/ibm/ibm-guardium-data-security-center.md) |
