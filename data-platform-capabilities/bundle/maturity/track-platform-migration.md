---
type: Maturity Track
id: track-platform-migration
title: Platform migration and portability
description: How safely and predictably the organisation moves workloads, code and data to new platforms, and how freely it can choose where the platform runs.
covers:
- platform-migration
- code-translation
- database-migration
- data-reconciliation
- deployment-options
- hybrid-data-plane
related_tracks: [track-storage, track-compute, track-ingestion, track-resilience]
levels:
- level: 1
  name: Initial
  summary: Migrations are hand-run projects, and where the platform runs was decided once and has not been revisited.
  criteria:
  - Moving a workload to a new platform means rewriting its SQL, procedures and jobs by hand, without an inventory of what exists on the old one.
  - Migrated outputs are checked by eye against a few reports from the old system.
  - Old and new platforms run side by side with no date for switching the old one off.
  - Nobody has recorded which workloads depend on features specific to one cloud provider or vendor.
  capabilities: []
- level: 2
  name: Managed
  summary: Migrations follow a written plan based on an inventory, databases move with migration tools, and deployment locations are recorded.
  criteria:
  - Before a migration, an inventory lists the tables, jobs, procedures, reports and users on the legacy platform, with usage taken from its logs.
  - Databases are moved with migration tools that convert schemas and keep source and target in step until cut-over.
  - Each migration wave has entry and exit criteria and a rollback plan agreed with the owners of the workloads it moves.
  - The cloud, region or site each workload runs in is recorded with the reason, such as residency, latency or an existing contract.
  capabilities: [platform-migration, database-migration, deployment-options]
- level: 3
  name: Defined
  summary: Code conversion, reconciliation and cut-over follow one documented, largely automated method.
  criteria:
  - SQL, stored procedures and ETL jobs are converted by translation tools, and the share converted without manual edits is recorded for each wave.
  - Every migrated table and report is reconciled with the legacy system by counts, control totals and sampled record comparisons before cut-over, and the results are kept.
  - Legacy and target platforms run in parallel for an agreed period, and the legacy system is switched off on a dated plan once reconciliation passes.
  - Where processing must stay inside the organisation's own network or cloud account, it runs in a customer-hosted data plane under the organisation's network and key controls, while the vendor operates the control plane.
  capabilities: [code-translation, data-reconciliation, hybrid-data-plane]
- level: 4
  name: Measured
  summary: Migration progress, defects and cost are measured against the plan, and exit from critical providers has been tested.
  criteria:
  - Progress is reported against plan as workloads, users and data volumes moved, together with the legacy running cost that remains.
  - Defects found after cut-over are counted per wave, and translation rules are corrected so later waves do not repeat them.
  - Run time and cost of each migrated workload are compared with its legacy baseline, and regressions are fixed before the legacy system is switched off.
  - Each critical workload has a documented exit plan from its platform provider, tested at least once by restoring its data and running its main jobs elsewhere.
  capabilities: []
- level: 5
  name: Optimising
  summary: Moving workloads between engines, clouds and deployment models is routine and planned from cost, risk and residency evidence.
  criteria:
  - Workload placement across clouds, regions and deployment models is reviewed at least yearly against cost, residency and resilience data, and moves are planned from the review.
  - Workloads built on open table formats and portable code are moved to another engine by pointing it at the same tables, and at least one such move has been completed without copying data.
  - Lessons from each migration update translation rules, inventory tooling and runbooks, and the effort per migrated workload falls from wave to wave.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up turns migration from a one-off rewrite with an uncertain end date into a repeatable method of inventory, automated conversion, reconciliation and dated cut-over, and keeps later moves between engines, clouds and deployment models within reach. The same evidence of what runs where, and what it depends on, supports exit plans for critical providers, which the EU Digital Operational Resilience Act requires financial entities to have for ICT services that support critical or important functions. Typical blockers are legacy estates nobody has inventoried, stored procedures and ETL jobs that translation tools only partly convert, validation left to users after cut-over, and legacy systems kept running because nobody can show that the new outputs match.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Migrations are hand-run projects, and where the platform runs was decided once and has not been revisited.

- Moving a workload to a new platform means rewriting its SQL, procedures and jobs by hand, without an inventory of what exists on the old one.
- Migrated outputs are checked by eye against a few reports from the old system.
- Old and new platforms run side by side with no date for switching the old one off.
- Nobody has recorded which workloads depend on features specific to one cloud provider or vendor.

## Level 2: Managed

Migrations follow a written plan based on an inventory, databases move with migration tools, and deployment locations are recorded.

- Before a migration, an inventory lists the tables, jobs, procedures, reports and users on the legacy platform, with usage taken from its logs.
- Databases are moved with migration tools that convert schemas and keep source and target in step until cut-over.
- Each migration wave has entry and exit criteria and a rollback plan agreed with the owners of the workloads it moves.
- The cloud, region or site each workload runs in is recorded with the reason, such as residency, latency or an existing contract.

**Capabilities first relied on:** [Platform migration](../capabilities/platform-operations/platform-migration.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md)

## Level 3: Defined

Code conversion, reconciliation and cut-over follow one documented, largely automated method.

- SQL, stored procedures and ETL jobs are converted by translation tools, and the share converted without manual edits is recorded for each wave.
- Every migrated table and report is reconciled with the legacy system by counts, control totals and sampled record comparisons before cut-over, and the results are kept.
- Legacy and target platforms run in parallel for an agreed period, and the legacy system is switched off on a dated plan once reconciliation passes.
- Where processing must stay inside the organisation's own network or cloud account, it runs in a customer-hosted data plane under the organisation's network and key controls, while the vendor operates the control plane.

**Capabilities first relied on:** [Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md)

## Level 4: Measured

Migration progress, defects and cost are measured against the plan, and exit from critical providers has been tested.

- Progress is reported against plan as workloads, users and data volumes moved, together with the legacy running cost that remains.
- Defects found after cut-over are counted per wave, and translation rules are corrected so later waves do not repeat them.
- Run time and cost of each migrated workload are compared with its legacy baseline, and regressions are fixed before the legacy system is switched off.
- Each critical workload has a documented exit plan from its platform provider, tested at least once by restoring its data and running its main jobs elsewhere.

## Level 5: Optimising

Moving workloads between engines, clouds and deployment models is routine and planned from cost, risk and residency evidence.

- Workload placement across clouds, regions and deployment models is reviewed at least yearly against cost, residency and resilience data, and moves are planned from the review.
- Workloads built on open table formats and portable code are moved to another engine by pointing it at the same tables, and at least one such move has been completed without copying data.
- Lessons from each migration update translation rules, inventory tooling and runbooks, and the effort per migrated workload falls from wave to wave.

# Capabilities in scope

[Code and SQL translation](../capabilities/platform-operations/code-translation.md), [Customer-hosted data plane](../capabilities/platform-operations/hybrid-data-plane.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Database migration](../capabilities/platform-operations/database-migration.md), [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md), [Platform migration](../capabilities/platform-operations/platform-migration.md)

# Related tracks

- [Storage and table management](track-storage.md): How well data is kept in durable, open, maintained tables that many engines can read, update and trust.
- [Compute and workload management](track-compute.md): How well compute is provisioned, isolated, scaled and tuned so that workloads meet performance targets at a known cost.
- [Ingestion and integration](track-ingestion.md): How reliably, quickly and safely the organisation brings data from source systems into the platform and keeps it in step with them.
- [Resilience and recovery](track-resilience.md): How well the platform withstands and recovers from data loss, corruption, ransomware and outages within agreed targets.

Levels follow the shared [maturity scale](maturity-scale.md).
