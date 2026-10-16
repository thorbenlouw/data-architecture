---
type: Maturity Track
id: track-data-sharing
title: Data sharing
description: How safely and efficiently data is shared between teams and with external parties without unnecessary copies.
covers:
- data-sharing
- internal-data-sharing
- external-data-sharing
- cross-region-sharing
- open-protocol-sharing
- data-marketplace
- data-clean-rooms
- application-sharing
related_tracks: [track-data-products, track-privacy, track-serving]
levels:
- level: 1
  name: Initial
  summary: Data is shared by sending extracts or copying tables.
  criteria:
  - Data goes to partners as file extracts or through database logins created for them.
  - Teams copy each other's tables into their own accounts or workspaces.
  - Nobody can produce a full list of external recipients of company data.
  capabilities: []
- level: 2
  name: Managed
  summary: Live shares replace copies for known teams and partners, under agreements recorded in a register.
  criteria:
  - Teams share live tables with each other through platform sharing features instead of copies.
  - External shares are read-only and created only for named partners under a signed agreement.
  - A register lists active shares, recipients and the agreements that cover them.
  capabilities: [internal-data-sharing, external-data-sharing]
- level: 3
  name: Defined
  summary: Sharing follows a standard approval workflow and reaches consumers on other platforms and regions.
  criteria:
  - Shares are requested and approved through a workflow that checks classification and usage terms before access is granted.
  - Consumers on other platforms receive live tables through an open sharing protocol instead of exports.
  - An internal marketplace lists shareable datasets and products with owners and terms, and subscription is self-service.
  - Consumers in other regions or clouds are served by managed replication that applies residency rules.
  capabilities: [open-protocol-sharing, data-marketplace, cross-region-sharing]
- level: 4
  name: Measured
  summary: Recipient usage is monitored, and joint analysis runs under enforced rules.
  criteria:
  - Each recipient's usage is logged and reported to the provider, and unused shares are revoked.
  - Joint analysis with partners runs in clean rooms that enforce each side's rules on joins, outputs and minimum group sizes.
  - Time to provision a share and the number of copies replaced by shares are tracked.
  - Freshness and quality terms attached to shared datasets are monitored.
  capabilities: [data-clean-rooms]
- level: 5
  name: Optimising
  summary: Data, code and models are distributed as products, and terms are reviewed from usage evidence.
  criteria:
  - Code, models and data are distributed as versioned applications that install and run in the consumer's environment.
  - Shared and commercial products are priced or charged back from measured use.
  - Terms, recipients and usage are reviewed periodically from logs, and terms are changed or shares withdrawn as a result.
  capabilities: [application-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up replaces file extracts and duplicated databases with live, governed shares that the provider can revoke, monitor and charge for, across clouds and platforms where needed. That reduces stale copies and makes it possible to prove who received what. Typical blockers are agreements that do not cover data use, consumers on other platforms, and no single view of what has already been shared and with whom.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Data is shared by sending extracts or copying tables.

- Data goes to partners as file extracts or through database logins created for them.
- Teams copy each other's tables into their own accounts or workspaces.
- Nobody can produce a full list of external recipients of company data.

## Level 2: Managed

Live shares replace copies for known teams and partners, under agreements recorded in a register.

- Teams share live tables with each other through platform sharing features instead of copies.
- External shares are read-only and created only for named partners under a signed agreement.
- A register lists active shares, recipients and the agreements that cover them.

**Capabilities first relied on:** [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md)

## Level 3: Defined

Sharing follows a standard approval workflow and reaches consumers on other platforms and regions.

- Shares are requested and approved through a workflow that checks classification and usage terms before access is granted.
- Consumers on other platforms receive live tables through an open sharing protocol instead of exports.
- An internal marketplace lists shareable datasets and products with owners and terms, and subscription is self-service.
- Consumers in other regions or clouds are served by managed replication that applies residency rules.

**Capabilities first relied on:** [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md)

## Level 4: Measured

Recipient usage is monitored, and joint analysis runs under enforced rules.

- Each recipient's usage is logged and reported to the provider, and unused shares are revoked.
- Joint analysis with partners runs in clean rooms that enforce each side's rules on joins, outputs and minimum group sizes.
- Time to provision a share and the number of copies replaced by shares are tracked.
- Freshness and quality terms attached to shared datasets are monitored.

**Capabilities first relied on:** [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md)

## Level 5: Optimising

Data, code and models are distributed as products, and terms are reviewed from usage evidence.

- Code, models and data are distributed as versioned applications that install and run in the consumer's environment.
- Shared and commercial products are priced or charged back from measured use.
- Terms, recipients and usage are reviewed periodically from logs, and terms are changed or shares withdrawn as a result.

**Capabilities first relied on:** [Data application distribution](../capabilities/data-sharing/application-sharing.md)

# Capabilities in scope

[Data sharing and collaboration](../capabilities/data-sharing/data-sharing.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Data application distribution](../capabilities/data-sharing/application-sharing.md), [Data clean rooms](../capabilities/data-sharing/data-clean-rooms.md), [Data marketplace](../capabilities/data-sharing/data-marketplace.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md), [Open-protocol sharing](../capabilities/data-sharing/open-protocol-sharing.md)

# Related tracks

- [Data products](track-data-products.md): How far data is managed as products with accountable owners, known consumers, explicit contracts and service levels.
- [Privacy](track-privacy.md): How reliably the organisation meets its obligations to the people its data describes, from purpose and consent to rights requests and de-identification.
- [Data serving](track-serving.md): How well curated data reaches applications, people and operational tools at the latency, volume and reliability they need.

Levels follow the shared [maturity scale](maturity-scale.md).
