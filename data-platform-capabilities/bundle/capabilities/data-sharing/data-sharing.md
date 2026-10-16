---
type: Capability
id: data-sharing
title: Data sharing and collaboration
description: Share data within and beyond the organisation safely, without unnecessary copies.
broader: []
related:
- data-products
- data-usage-rights
- privacy-enhancing-technologies
- audit-logging
- managed-file-transfer
depends_on: [access-control]
order: 16
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data sharing covers how data reaches people and organisations beyond the team that produces it. Traditionally that meant extracts: files sent over SFTP or copies loaded into another system, each going stale and each needing its own security. Modern platforms instead grant a consumer read access to live tables in place, so the provider keeps one copy, controls who sees it and can revoke access at any time.

The domain divides by audience and trust. Internal sharing connects teams, accounts and workspaces within one organisation. External sharing reaches customers, partners and suppliers, and extends across regions, clouds and other vendors' platforms through replication and open protocols. A marketplace makes shared data discoverable and handles subscription, and sometimes payment.

Two capabilities serve cases where the consumer should not see the data at all. Clean rooms let parties analyse combined data while each limits what the others can learn, and application distribution sends code and models to run beside the consumer's data. Common to all of them are usage terms, auditing of consumer access and controls on personal data.

# Key considerations

- Live sharing removes copies but ties consumers to your platform's availability and performance. Agree service levels and who pays for consumer queries.
- Share curated, documented data products rather than raw tables, so internal changes do not break consumers.
- Record usage terms with each share and audit what consumers query, especially for personal or licensed data.
- Check whether sharing works across accounts, regions and other platforms, or only between users of one vendor in one region.

# Questions to ask

- Who needs data from you, and whose data do you need: internal teams, customers, partners or regulators?
- How is data exchanged today, and how many copies does that create?
- Does any shared data include personal, licensed or commercially sensitive content?
- Must consumers on other platforms or clouds be supported?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Data application distribution](application-sharing.md), [Data clean rooms](data-clean-rooms.md), [Data marketplace](data-marketplace.md), [External data sharing](external-data-sharing.md), [Internal data sharing](internal-data-sharing.md) |
| Related | [Serving and activation](../serving/serving.md), [Data products](../data-products/data-products.md), [Audit logging](../security/audit-logging.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [Managed file transfer](../ingestion-integration/managed-file-transfer.md), [Privacy-enhancing technologies](../governance/privacy-enhancing-technologies.md), [Synthetic data generation](../development-lifecycle/synthetic-data.md) |
| Depends on | [Access control](../security/access-control.md) |

# Where it appears

- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 44 technologies; see their pages.
