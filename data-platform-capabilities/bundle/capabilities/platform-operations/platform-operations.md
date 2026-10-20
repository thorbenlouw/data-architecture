---
type: Capability
id: platform-operations
title: Platform operations
description: Run the data platform itself, including provisioning, tenancy, cost, monitoring and resilience.
broader: []
related: [development-lifecycle, security, governance, compute]
order: 19
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Platform operations is the work of running the data platform as a service for the teams that build on it. One group of capabilities creates and shapes the environment. Infrastructure as code defines accounts, workspaces, compute, networks and permissions; multi-tenancy divides shared foundations into isolated areas for teams or domains; self-service provisioning lets teams create what they need from approved templates. A second group shows what is happening: platform observability, pipeline monitoring, query performance analysis and usage telemetry.

A third group handles money and risk. Cost management attributes spend, sets budgets and finds savings, including for model and agent use. Backup and disaster recovery protect against loss and outages, and resilience testing shows that recovery works. Deployment options decide where the platform runs: one cloud or several, on premises, or with processing inside your own account. Sustainability reporting adds energy and carbon to the measures the platform is judged by.

Platform migration covers moving onto the platform from legacy systems, often the largest piece of operational work an organisation does. These capabilities matter more as the number of teams grows. One team can run a platform by hand; twenty need automation, guard rails and clear charging. Development and DataOps decide what is deployed; platform operations provides and runs the places it is deployed to.

# Key considerations

- Run the platform as a product with named owners, a roadmap and service levels, not as a project that ends at go-live.
- Automate from the start. Workspaces, permissions and budgets created by hand drift and cannot be recreated reliably after an incident.
- Decide the tenancy model early: how teams, domains and environments map to accounts, workspaces and catalogues. It is hard to change once data and permissions depend on it.
- Agree recovery objectives for each tier of data and workload before choosing backup and replication designs.
- Show cost and usage data to the teams who generate it, not only to the central team.

# Questions to ask

- How many teams will build on the platform, and how fast is that number growing?
- Who is on call for the platform, and what service levels do teams expect?
- How much data loss and downtime can the business tolerate for its most important data?
- How is platform spend reported and recovered from teams today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Backup and disaster recovery](business-continuity.md), [Cost management](cost-management.md), [Hybrid and multi-cloud deployment](deployment-options.md), [Infrastructure as code](infrastructure-as-code.md), [Multi-tenancy and workspace isolation](multi-tenancy.md), [Platform migration](platform-migration.md), [Platform observability](platform-observability.md), [Resource configuration guardrails](configuration-guardrails.md), [Runtime and environment management](../development-lifecycle/runtime-management.md), [Self-service provisioning](self-service-provisioning.md), [Sustainability and carbon management](sustainability-reporting.md) |
| Related | [Query and compute](../compute/compute.md), [Governance and compliance](../governance/governance.md), [Security and access](../security/security.md), [Development and DataOps](../development-lifecycle/development-lifecycle.md) |

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 214 technologies; see their pages.
