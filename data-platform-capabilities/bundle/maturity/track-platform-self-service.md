---
type: Maturity Track
id: track-platform-self-service
title: Platform self-service
description: How far teams can obtain, run and observe what they need on the shared platform without waiting for a central team.
covers:
- infrastructure-as-code
- multi-tenancy
- self-service-provisioning
- platform-observability
- pipeline-monitoring
- query-performance-analysis
- system-telemetry
- runtime-management
- configuration-guardrails
- platform-incident-management
related_tracks: [track-path-to-live, track-security, track-finops, track-orchestration]
levels:
- level: 1
  name: Initial
  summary: A central team builds environments by hand in response to tickets.
  criteria:
  - Workspaces, clusters and permissions are created by hand in consoles after a ticket.
  - Environments differ in ways nobody has written down.
  - Job failures are found by reading logs on the machine where the job ran.
  capabilities: []
- level: 2
  name: Managed
  summary: Core resources are defined as code, and teams can see their own pipeline runs and failures.
  criteria:
  - Core platform resources are defined as code and applied from version control.
  - Logs and metrics from all workspaces are collected in one monitoring service, where each team can see its own pipeline runs, failures and durations.
  - Teams have separate workspaces or projects, though they share catalogues and compute.
  capabilities: [infrastructure-as-code, platform-observability, pipeline-monitoring]
- level: 3
  name: Defined
  summary: Teams provision approved resources from templates into their own tenancy, run on published runtimes and can query their own telemetry.
  criteria:
  - Teams create approved workspaces, pipelines and resources from templates through a portal or command, with security and tagging applied automatically.
  - Each domain or team has its own workspace, catalogue area and budget on shared foundations.
  - Platform usage, billing and operational data are available to every team as queryable tables.
  - Users can see query history and plans for their own work and tune it themselves.
  - Notebooks, jobs and model serving run on runtime versions and images that the platform team publishes with a support end date, and teams upgrade by changing one version setting.
  capabilities:
  - self-service-provisioning
  - multi-tenancy
  - system-telemetry
  - query-performance-analysis
  - runtime-management
- level: 4
  name: Measured
  summary: Provisioning time, template adoption and platform service levels are measured against targets, and configuration rules are enforced automatically.
  criteria:
  - Time from request to a working workspace is measured against a target, such as under one hour.
  - Logs, metrics and traces from jobs, queries and services are correlated in one place, with service-level objectives for platform components.
  - Policies limit which resources teams can create and how they are configured, such as allowed sizes, regions, tags and network settings, and resources that break the rules or drift from their code definitions are reported automatically.
  - The share of resources created from templates rather than by hand is reported.
  capabilities: [configuration-guardrails]
- level: 5
  name: Optimising
  summary: Templates, guardrails and quotas evolve from usage data and incident reviews.
  criteria:
  - Templates are revised from usage data and developer feedback, and adoption of each version is tracked.
  - Platform outages are handled through an on-call rota and runbooks, each major incident has a blameless review, and recurring causes become tracked template, guardrail or runbook changes.
  - Capacity and quota needs per tenant are forecast from telemetry, and limits are raised before teams reach them.
  capabilities: [platform-incident-management]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up turns the platform team from a ticket queue into the owner of templates, guardrails and telemetry, so domain teams create workspaces and pipelines in minutes and see their own jobs, failures and usage. It corresponds to the self-serve data platform principle of data mesh. Typical blockers are hand-built environments that cannot be reproduced, isolation that is all or nothing, and platform teams measured on tickets closed rather than on teams onboarded.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

A central team builds environments by hand in response to tickets.

- Workspaces, clusters and permissions are created by hand in consoles after a ticket.
- Environments differ in ways nobody has written down.
- Job failures are found by reading logs on the machine where the job ran.

## Level 2: Managed

Core resources are defined as code, and teams can see their own pipeline runs and failures.

- Core platform resources are defined as code and applied from version control.
- Logs and metrics from all workspaces are collected in one monitoring service, where each team can see its own pipeline runs, failures and durations.
- Teams have separate workspaces or projects, though they share catalogues and compute.

**Capabilities first relied on:** [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md)

## Level 3: Defined

Teams provision approved resources from templates into their own tenancy, run on published runtimes and can query their own telemetry.

- Teams create approved workspaces, pipelines and resources from templates through a portal or command, with security and tagging applied automatically.
- Each domain or team has its own workspace, catalogue area and budget on shared foundations.
- Platform usage, billing and operational data are available to every team as queryable tables.
- Users can see query history and plans for their own work and tune it themselves.
- Notebooks, jobs and model serving run on runtime versions and images that the platform team publishes with a support end date, and teams upgrade by changing one version setting.

**Capabilities first relied on:** [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md)

## Level 4: Measured

Provisioning time, template adoption and platform service levels are measured against targets, and configuration rules are enforced automatically.

- Time from request to a working workspace is measured against a target, such as under one hour.
- Logs, metrics and traces from jobs, queries and services are correlated in one place, with service-level objectives for platform components.
- Policies limit which resources teams can create and how they are configured, such as allowed sizes, regions, tags and network settings, and resources that break the rules or drift from their code definitions are reported automatically.
- The share of resources created from templates rather than by hand is reported.

**Capabilities first relied on:** [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md)

## Level 5: Optimising

Templates, guardrails and quotas evolve from usage data and incident reviews.

- Templates are revised from usage data and developer feedback, and adoption of each version is tracked.
- Platform outages are handled through an on-call rota and runbooks, each major incident has a blameless review, and recurring causes become tracked template, guardrail or runbook changes.
- Capacity and quota needs per tenant are forecast from telemetry, and limits are raised before teams reach them.

**Capabilities first relied on:** [Platform incident management](../capabilities/platform-operations/platform-incident-management.md)

# Capabilities in scope

[Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../capabilities/platform-operations/query-performance-analysis.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md), [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md)

# Related tracks

- [Path to live](track-path-to-live.md): How safely, quickly and repeatably changes to data and AI workloads move from a developer's first commit to production.
- [Security and access control](track-security.md): How well data is protected from unauthorised access, loss and misuse, from identity through fine-grained access to threat detection.
- [FinOps](track-finops.md): How well the organisation understands, allocates and controls what the data platform costs, relative to the value it delivers.
- [Orchestration](track-orchestration.md): How dependably the organisation schedules, sequences and recovers the jobs that move and transform data.

Levels follow the shared [maturity scale](maturity-scale.md).
