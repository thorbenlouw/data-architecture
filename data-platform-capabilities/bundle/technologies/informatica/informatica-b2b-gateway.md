---
type: Technology
id: informatica-b2b-gateway
title: Informatica B2B Gateway
description: Exchanges EDI messages and files with trading partners and maps them to back-end systems using prebuilt mappings, with a partners portal for tracking exchanged files.
platform: platform-informatica
kind: managed-service
availability: ga
realises: [managed-file-transfer, b2b-edi-integration]
resource: https://onlinehelp.informatica.com/IICS/prod/mde/en/zz-cloud-helpoverview/Help_for_Other_Services.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The companion B2B Partners Portal lets partners track and monitor their own file exchanges.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) (Ingestion and integration) (primary): Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.
- [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md) (Ingestion and integration): Exchange structured business documents such as orders and invoices with trading partners using EDI standards.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Transfer Family](../aws/aws-transfer-family.md) | [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md) | [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [B2B and EDI integration](../../capabilities/ingestion-integration/b2b-edi-integration.md), [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
