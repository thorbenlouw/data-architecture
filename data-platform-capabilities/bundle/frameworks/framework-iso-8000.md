---
type: Framework
id: framework-iso-8000
title: ISO 8000 (data quality)
description: A series of international standards on data quality, covering concepts, quality management processes, profiling, rules, master data exchange and sensor data.
aliases: [ISO 8000 series, ISO 8000-8, ISO 8000-61, ISO 8000-110]
kind: standard
publisher: ISO (TC 184/SC 4)
resource: https://www.iso.org/standard/81745.html
related: [framework-dama-dmbok, framework-edm-dcam]
applies_to: [usecase-customer-360, usecase-iot-predictive-maintenance, persona-data-steward, persona-cdo]
mappings:
- ref: ISO 8000-8 – Concepts and measuring
  summary: Defines what data quality means, separating syntactic, semantic and pragmatic quality, and how each can be measured.
  capabilities: [data-quality-scorecards, data-quality-rules, data-profiling]
- ref: ISO 8000-51 – Exchange of data policy statements
  summary: Specifies how organisations state and exchange their data governance policies.
  capabilities: [data-policy-management, data-contracts]
- ref: ISO 8000-61 – Data quality management process reference model
  summary: Describes the processes for planning, controlling, assuring and improving data quality.
  capabilities:
  - data-quality-rules
  - data-observability
  - data-quality-scorecards
  - data-issue-management
  - data-cleansing
- ref: ISO 8000-62 to 8000-65 – Process maturity assessment and measurement
  summary: Gives methods and questionnaires for assessing how mature data quality management processes are.
  capabilities: [data-quality-scorecards, governance-metrics]
- ref: ISO/TS 8000-81 – Data profiling
  summary: Describes how to profile data to understand its content and quality.
  capabilities: [data-profiling]
- ref: ISO/TS 8000-82 – Creating data rules
  summary: Describes how to write rules that data must satisfy.
  capabilities: [data-quality-rules]
- ref: ISO 8000-100 and 8000-110 – Master data exchange and conformance to data specification
  summary: Sets requirements for exchanging master data that conforms to a stated specification with explicit semantic encoding.
  capabilities: [master-data-management, reference-data-management, data-contracts]
- ref: ISO 8000-115 to 8000-119 – Quality identifiers
  summary: Sets rules for unambiguous, resolvable identifiers, applied to legal entities, locations and other objects.
  capabilities: [master-data-management, entity-resolution, reference-data-management]
- ref: ISO 8000-120 – Provenance
  summary: Requires master data to carry a record of where each value came from.
  capabilities: [data-lineage, survivorship, master-data-management]
- ref: ISO 8000-130 and 8000-140 – Accuracy and completeness
  summary: Sets requirements for stating and exchanging the accuracy and completeness of master data.
  capabilities: [data-quality-rules, data-quality-scorecards]
- ref: ISO 8000-150 – Roles and responsibilities
  summary: Defines the roles needed to manage data quality.
  capabilities: [data-ownership, stewardship-workflows]
- ref: ISO 8000-210 to 8000-230 – Sensor data
  summary: Covers quality characteristics, measurement and cleansing of sensor data.
  capabilities: [iot-ingestion, time-series-data, data-cleansing, data-anomaly-detection]
- ref: ISO/CD TR 8000-320 – AI training data quality (in development)
  summary: Will give guidance on the quality of data used to train AI in manufacturing.
  capabilities: [training-dataset-management, data-labelling, data-quality-rules, data-profiling]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ISO 8000 is a multi-part series: part 1 (2022, reconfirmed in 2024) gives the overview, part 2 the vocabulary, and further parts cover data quality management, maturity assessment, profiling, data rules, master data exchange, identifiers and sensor data. It is used mainly in manufacturing, supply chain, defence and master data programmes, and less often as a whole by analytics teams, but its parts on profiling, rules, provenance and quality management give vendor-neutral definitions that platform quality capabilities can be measured against. Work in progress includes a requirements standard for information and data management systems (part 3) and a technical report on AI training data quality for smart manufacturing (part 320).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| ISO 8000-8 – Concepts and measuring | Defines what data quality means, separating syntactic, semantic and pragmatic quality, and how each can be measured. | [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data profiling](../capabilities/data-quality/data-profiling.md) |
| ISO 8000-51 – Exchange of data policy statements | Specifies how organisations state and exchange their data governance policies. | [Policy management](../capabilities/governance/data-policy-management.md), [Data contracts](../capabilities/data-products/data-contracts.md) |
| ISO 8000-61 – Data quality management process reference model | Describes the processes for planning, controlling, assuring and improving data quality. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md) |
| ISO 8000-62 to 8000-65 – Process maturity assessment and measurement | Gives methods and questionnaires for assessing how mature data quality management processes are. | [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md) |
| ISO/TS 8000-81 – Data profiling | Describes how to profile data to understand its content and quality. | [Data profiling](../capabilities/data-quality/data-profiling.md) |
| ISO/TS 8000-82 – Creating data rules | Describes how to write rules that data must satisfy. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md) |
| ISO 8000-100 and 8000-110 – Master data exchange and conformance to data specification | Sets requirements for exchanging master data that conforms to a stated specification with explicit semantic encoding. | [Master data management](../capabilities/master-data/master-data-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data contracts](../capabilities/data-products/data-contracts.md) |
| ISO 8000-115 to 8000-119 – Quality identifiers | Sets rules for unambiguous, resolvable identifiers, applied to legal entities, locations and other objects. | [Master data management](../capabilities/master-data/master-data-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Reference data management](../capabilities/master-data/reference-data-management.md) |
| ISO 8000-120 – Provenance | Requires master data to carry a record of where each value came from. | [Data lineage](../capabilities/metadata/data-lineage.md), [Merge and survivorship](../capabilities/master-data/survivorship.md), [Master data management](../capabilities/master-data/master-data-management.md) |
| ISO 8000-130 and 8000-140 – Accuracy and completeness | Sets requirements for stating and exchanging the accuracy and completeness of master data. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) |
| ISO 8000-150 – Roles and responsibilities | Defines the roles needed to manage data quality. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md) |
| ISO 8000-210 to 8000-230 – Sensor data | Covers quality characteristics, measurement and cleansing of sensor data. | [IoT and telemetry ingestion](../capabilities/ingestion-integration/iot-ingestion.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Data anomaly detection](../capabilities/data-quality/data-anomaly-detection.md) |
| ISO/CD TR 8000-320 – AI training data quality (in development) | Will give guidance on the quality of data used to train AI in manufacturing. | [Training and evaluation dataset management](../capabilities/machine-learning/training-dataset-management.md), [Data labelling](../capabilities/machine-learning/data-labelling.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data profiling](../capabilities/data-quality/data-profiling.md) |

# Related frameworks

- [DAMA-DMBOK 2](framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
- [DCAM v3](framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.

# Applies to

- [Customer 360](../use-cases/usecase-customer-360.md) (use case): Give every channel a single, trusted view of each customer.
- [IoT predictive maintenance](../use-cases/usecase-iot-predictive-maintenance.md) (use case): Analyse sensor telemetry to predict equipment failures before they happen.
- [Data steward](../personas/persona-data-steward.md) (persona): Looks after the definition, quality and proper use of data in a business domain.
- [Chief data officer](../personas/persona-cdo.md) (persona): Accountable for the organisation's data strategy, value, risk and governance.
