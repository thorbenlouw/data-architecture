---
type: Technology
id: aws-transfer-family
title: AWS Transfer Family
description: Managed SFTP, FTPS, FTP and AS2 endpoints that store exchanged files directly in S3 or EFS.
formerly: [AWS Transfer for SFTP]
platform: platform-aws
kind: managed-service
availability: ga
realises: [managed-file-transfer]
resource: https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed workflows can post-process uploaded files, and SFTP connectors push or pull files from partner servers. Pairs with S3 event notifications or Redshift auto-copy to start ingestion.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) (Ingestion and integration) (primary): Exchange files securely with partners over SFTP, FTPS or AS2, with tracking and retries.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Logic Apps](../microsoft/azure-logic-apps.md) | [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica B2B Gateway](../informatica/informatica-b2b-gateway.md) | [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Integration Suite](../sap/sap-integration-suite.md) | [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache NiFi](../open-source/apache-nifi.md) | [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Boomi Enterprise Platform](../independent/boomi-enterprise-platform.md) | [Managed file transfer](../../capabilities/ingestion-integration/managed-file-transfer.md) |
