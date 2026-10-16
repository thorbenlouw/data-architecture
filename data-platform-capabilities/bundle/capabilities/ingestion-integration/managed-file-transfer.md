---
type: Capability
id: managed-file-transfer
title: Managed file transfer
description: Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.
aliases: [MFT, B2B file exchange]
broader: [ingestion-integration]
related: [file-ingestion, b2b-edi-integration, audit-logging, network-security]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed file transfer (MFT) runs the secure endpoints through which partners send and receive files, and the controls around them: an account and keys per partner, encryption, scheduled transfers, automatic retries, delivery receipts and a full record of who sent what and when. A bank might receive daily statement files from correspondent banks over SFTP; the MFT service checks each file's integrity, decrypts it with OpenPGP and moves it to a landing area where file ingestion picks it up.

Many industries still exchange data with partners mainly as files, and contracts or regulators often require proof of delivery. MFT replaces scattered FTP servers and scripts with one governed service. AS2 adds signed receipts that prove delivery and is common in retail and supply chains. MFT ends at the landing area: parsing and loading belong to file ingestion, and interpreting business documents such as orders belongs to B2B and EDI integration.

# Key considerations

- Track partner keys and certificates and their expiry dates. Expired certificates are a common cause of failed transfers.
- Restrict partner access by account and source address, and keep partner-facing endpoints outside the core platform network.
- Keep transfer logs and receipts for as long as contracts or regulators require.
- Define what happens with late, missing or duplicate files, and who is alerted.

# Questions to ask

- How many partners exchange files, over which protocols and how often?
- Do contracts or regulations require proof of delivery or non-repudiation?
- Who onboards new partners and manages their credentials today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Data sharing and collaboration](../data-sharing/data-sharing.md), [Audit logging](../security/audit-logging.md), [B2B and EDI integration](b2b-edi-integration.md), [Data export](../serving/data-export.md), [External data sharing](../data-sharing/external-data-sharing.md), [File ingestion](file-ingestion.md), [Network security](../security/network-security.md) |

# Where it appears

- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS Transfer Family | [AWS Transfer Family](../../technologies/aws/aws-transfer-family.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Logic Apps](../../technologies/microsoft/azure-logic-apps.md) |
| [Informatica](../../platforms/platform-informatica.md) | B2B Gateway | [Informatica B2B Gateway](../../technologies/informatica/informatica-b2b-gateway.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Integration Suite](../../technologies/sap/sap-integration-suite.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache NiFi](../../technologies/open-source/apache-nifi.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Boomi Enterprise Platform](../../technologies/independent/boomi-enterprise-platform.md) |
