---
type: Capability
id: platform-incident-management
title: Platform incident management
description: Detect, escalate and resolve platform outages and degradations through on-call rotas, runbooks and post-incident reviews.
aliases: [on-call, SRE for data platforms]
broader: [platform-observability]
related:
- data-issue-management
- ai-incident-management
- pipeline-monitoring
- cross-region-failover
- data-slas
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An incident is an unplanned loss or degradation of service, such as a query engine refusing connections, the orchestrator no longer scheduling jobs, or a storage outage in one region. An alert opens the incident, pages the engineer on call and sets a severity, which decides who else joins and how often stakeholders get updates. Responders follow runbooks, which are written steps for known failures, keep a timeline of actions, and restore service before hunting for the root cause. Afterwards a blameless post-incident review records what happened, why, and what will stop it recurring.

It matters once other teams, products or customers depend on the platform and have their own service levels to meet. Keep it distinct from data issue management, which deals with wrong or late data in particular datasets, and from AI incident management, which covers harm caused by AI systems and may require reports to regulators. The three often share tooling and should be linked when one incident causes another.

# Key considerations

- Define severity by impact on consumers, such as how many critical pipelines or users are affected, not by which component failed.
- Page on symptoms users feel, such as failed queries or missed freshness targets, rather than on every internal metric. Noisy paging teaches people to ignore alerts.
- Many incidents start with the cloud provider or a vendor. Know how to check their status, open priority support cases and record their part in the timeline.
- Tell data consumers about incidents through a status page or channel, so they do not each raise duplicate tickets.
- Track review actions to completion and measure time to detect and time to restore. Reviews whose actions are never done change nothing.

# Questions to ask

- What service levels does the platform promise its consumers, and which failures would break them?
- Who is on call for the platform out of hours, and is the rota sustainable for the team's size?
- How, and how quickly, are consumers told about outages today?
- Which recent incidents have happened more than once, and why?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform observability](platform-observability.md) |
| Related | [AI incident management](../governance/ai-incident-management.md), [Cross-region replication and failover](cross-region-failover.md), [Data breach response](../security/data-breach-response.md), [Data issue management](../data-quality/data-issue-management.md), [Data service levels](../data-products/data-slas.md), [Pipeline monitoring and alerting](pipeline-monitoring.md) |

# Where it appears

- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 5, Optimising)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter II – ICT risk management (Articles 5 to 16); Articles 11 and 12 – Response and recovery; backup, restoration and recovery; Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Independent vendors](../../platforms/platform-independent.md) |  | [PagerDuty](../../technologies/independent/pagerduty.md) |
