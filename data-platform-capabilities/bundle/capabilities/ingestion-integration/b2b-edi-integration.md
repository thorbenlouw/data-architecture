---
type: Capability
id: b2b-edi-integration
title: B2B and EDI integration
description: Exchange structured business documents such as orders and invoices with trading partners using EDI standards.
aliases: [EDI, X12, EDIFACT, trading partner integration]
broader: [ingestion-integration]
related: [managed-file-transfer, application-integration, data-reconciliation]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Electronic data interchange (EDI) is the exchange of business documents between organisations in standard structured formats, chiefly ANSI X12 in North America and UN/EDIFACT elsewhere, with industry subsets of each. A supplier receives a purchase order as an X12 850 message, returns an acknowledgement, and later sends an advance ship notice and an invoice. An EDI capability translates these messages to and from internal structures, validates them against each partner's agreed specification and tracks acknowledgements so nothing goes missing.

Retail, manufacturing, logistics and healthcare still run much of their supply chains on EDI, and many trading partners insist on it. For the data platform, the value is the transaction data: orders, shipments and invoices from EDI flows are a dependable source for supply chain analytics. Transport is often AS2 or a value-added network, which overlaps with managed file transfer. API-based exchange is growing, but EDI persists because moving every partner at once is impractical.

# Key considerations

- Each partner usually has its own variant of the standard. Keep partner-specific mappings versioned and tested.
- Track functional acknowledgements and alert on missing ones. An unacknowledged order can mean a lost sale or a late shipment.
- Store both the raw message and its parsed form, so disputes can be checked against what was actually sent.
- Healthcare and other regulated EDI flows carry personal data and need the same access controls as other sensitive data.

# Questions to ask

- How many trading partners use EDI, and which document types and standards do they use?
- Is EDI handled in-house, by a service provider or through a value-added network?
- Which analyses depend on EDI transaction data?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Application integration](application-integration.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Managed file transfer](managed-file-transfer.md), [Product information management](../master-data/product-information-management.md) |

# Where it appears

- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Logic Apps](../../technologies/microsoft/azure-logic-apps.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica B2B Gateway](../../technologies/informatica/informatica-b2b-gateway.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Integration Suite](../../technologies/sap/sap-integration-suite.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Boomi Enterprise Platform](../../technologies/independent/boomi-enterprise-platform.md), [MuleSoft Anypoint Platform](../../technologies/independent/mulesoft-anypoint-platform.md) |
