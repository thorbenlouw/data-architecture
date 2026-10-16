---
type: Maturity Track
id: track-data-quality
title: Data quality and observability
description: How systematically the organisation defines, measures, monitors and fixes the fitness of data for its intended uses.
covers:
- data-quality
- data-profiling
- data-quality-rules
- data-quality-scorecards
- data-observability
- freshness-monitoring
- data-anomaly-detection
- data-cleansing
- data-reconciliation
- bad-data-quarantine
- data-issue-management
- unstructured-data-quality
- data-trust-indicators
related_tracks: [track-lineage, track-data-products, track-master-data, track-ml-development]
levels:
- level: 1
  name: Initial
  summary: Consumers find quality problems, and fixes are made by hand downstream.
  criteria:
  - Bad data is noticed when a report looks wrong, and corrections are made directly in downstream tables.
  - Checks, where they exist, are queries an individual runs when they remember.
  - No record is kept of past quality incidents or their causes.
  capabilities: []
- level: 2
  name: Managed
  summary: Teams profile sources, run rules in their pipelines and track incidents.
  criteria:
  - New sources are profiled for completeness, value distributions and key uniqueness before pipelines are built on them.
  - Completeness, validity and uniqueness rules run in the pipelines for important tables, and failures stop the load or alert the team.
  - Quality incidents are logged in a tracker with an owner and status.
  - Arrival of key tables is checked against an expected time.
  capabilities: [data-profiling, data-quality-rules, data-issue-management, freshness-monitoring]
- level: 3
  name: Defined
  summary: Shared rule formats, quarantine, reconciliation and baseline monitoring apply to all production data.
  criteria:
  - Rules are written in a shared format, stored with pipeline code and reused across teams.
  - Records that fail checks go to a quarantine table with the failed rule recorded and can be replayed after correction.
  - Data moved between systems is reconciled by counts and control totals, and results are kept as evidence.
  - Freshness, volume and schema changes are monitored on every production table, not only those with hand-written rules.
  - Addresses, names and codes are standardised by shared cleansing functions instead of logic in each pipeline.
  capabilities: [bad-data-quarantine, data-reconciliation, data-observability, data-cleansing]
- level: 4
  name: Measured
  summary: Quality is scored against targets agreed with consumers, anomalies are detected without hand-set thresholds, and consumers see trust indicators where they use data.
  criteria:
  - Scorecards publish quality by dataset, domain and dimension against targets agreed with consumers.
  - Anomaly detection learns normal volumes and distributions and alerts on deviations without hand-written thresholds.
  - Time to detect and time to resolve quality incidents are measured per domain.
  - Consumers see, in the tools where they use data, whether each dataset, dashboard or AI answer is certified, fresh, passing its checks and free of open incidents.
  - Document collections used for retrieval or training are scored for duplication, staleness and sensitive content.
  capabilities: [data-quality-scorecards, data-anomaly-detection, unstructured-data-quality, data-trust-indicators]
- level: 5
  name: Optimising
  summary: Causes are fixed at source, and rules and investment are tuned from incident evidence.
  criteria:
  - Recurring incident causes are analysed, and fixes go into source systems or producer contracts rather than downstream code.
  - Rules that never fail or always fail are reviewed and tuned or removed.
  - The cost of quality incidents, such as rework and late reports, is estimated and used to prioritise investment.
  - Checks for new datasets are generated from contracts and profiling results, and owners review them instead of writing them.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up shifts quality from consumers spotting wrong numbers to producers catching problems before publication, with named owners, measured results and causes fixed at source. ISO 8000-61 describes the plan, control, assure and improve processes behind this, ISO 8000-62 to 8000-65 provide a formal process maturity assessment, and DCAM's data quality component scores similar evidence; this track focuses on what can be checked on the platform. Typical blockers are rules written without knowing what consumers need, alert floods that teams learn to ignore, and owners with no time to fix issues upstream.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Consumers find quality problems, and fixes are made by hand downstream.

- Bad data is noticed when a report looks wrong, and corrections are made directly in downstream tables.
- Checks, where they exist, are queries an individual runs when they remember.
- No record is kept of past quality incidents or their causes.

## Level 2: Managed

Teams profile sources, run rules in their pipelines and track incidents.

- New sources are profiled for completeness, value distributions and key uniqueness before pipelines are built on them.
- Completeness, validity and uniqueness rules run in the pipelines for important tables, and failures stop the load or alert the team.
- Quality incidents are logged in a tracker with an owner and status.
- Arrival of key tables is checked against an expected time.

**Capabilities first relied on:** [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md)

## Level 3: Defined

Shared rule formats, quarantine, reconciliation and baseline monitoring apply to all production data.

- Rules are written in a shared format, stored with pipeline code and reused across teams.
- Records that fail checks go to a quarantine table with the failed rule recorded and can be replayed after correction.
- Data moved between systems is reconciled by counts and control totals, and results are kept as evidence.
- Freshness, volume and schema changes are monitored on every production table, not only those with hand-written rules.
- Addresses, names and codes are standardised by shared cleansing functions instead of logic in each pipeline.

**Capabilities first relied on:** [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md)

## Level 4: Measured

Quality is scored against targets agreed with consumers, anomalies are detected without hand-set thresholds, and consumers see trust indicators where they use data.

- Scorecards publish quality by dataset, domain and dimension against targets agreed with consumers.
- Anomaly detection learns normal volumes and distributions and alerts on deviations without hand-written thresholds.
- Time to detect and time to resolve quality incidents are measured per domain.
- Consumers see, in the tools where they use data, whether each dataset, dashboard or AI answer is certified, fresh, passing its checks and free of open incidents.
- Document collections used for retrieval or training are scored for duplication, staleness and sensitive content.

**Capabilities first relied on:** [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md)

## Level 5: Optimising

Causes are fixed at source, and rules and investment are tuned from incident evidence.

- Recurring incident causes are analysed, and fixes go into source systems or producer contracts rather than downstream code.
- Rules that never fail or always fail are reviewed and tuned or removed.
- The cost of quality incidents, such as rework and late reports, is estimated and used to prioritise investment.
- Checks for new datasets are generated from contracts and profiling results, and owners review them instead of writing them.

# Capabilities in scope

[Data quality and observability](../capabilities/data-quality/data-quality.md), [Bad-data quarantine](../capabilities/data-quality/bad-data-quarantine.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Unstructured data quality](../capabilities/data-quality/unstructured-data-quality.md)

# Related tracks

- [Lineage](track-lineage.md): How completely and automatically the organisation can show where data came from, how it was changed and what depends on it.
- [Data products](track-data-products.md): How far data is managed as products with accountable owners, known consumers, explicit contracts and service levels.
- [Master and reference data](track-master-data.md): How consistently core business entities and shared code lists are identified, matched and maintained across systems.
- [ML development](track-ml-development.md): How repeatably the organisation turns data into trained, evaluated and documented models.

Levels follow the shared [maturity scale](maturity-scale.md).
