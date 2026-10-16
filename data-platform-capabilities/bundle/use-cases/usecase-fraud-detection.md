---
type: Use Case
id: usecase-fraud-detection
title: Real-time fraud detection
description: Score transactions in milliseconds and block or flag suspicious ones.
aliases: [transaction fraud, payment fraud scoring]
requires:
- {capability: real-time-inference, level: 3, why: 'Scores must return within the payment authorisation window, typically tens of milliseconds.'}
- {capability: online-feature-store, level: 3, why: Recent-behaviour features for each card or account must be read in milliseconds at scoring time.}
- {capability: stream-processing, level: 3, why: Counts and amounts over sliding windows are computed continuously from the transaction stream.}
- {capability: event-streaming, level: 3, why: 'Transactions and outcomes flow as durable, replayable events between payment systems, features and models.'}
- {capability: point-in-time-joins, level: 3, why: 'Training must use features as they stood at each transaction, or the model will not behave the same live.'}
- {capability: model-training, level: 2, why: Models are retrained regularly on recent labelled fraud.}
- {capability: model-registry, level: 3, why: 'The version scoring live payments must be controlled, approved and quick to roll back.'}
- {capability: inference-logging, level: 3, why: 'Every decision, with its inputs, model version and score, is kept for disputes, audit and retraining.'}
- {capability: drift-detection, level: 3, why: 'Fraudsters adapt, so changes in inputs and scores must be caught before labels arrive.'}
- {capability: model-performance-monitoring, level: 3, why: Detection and false-positive rates are tracked as confirmed fraud and chargebacks come in.}
- {capability: model-explainability, level: 2, why: Investigators and customers need reason codes for declines.}
- {capability: human-oversight, level: 2, why: 'Borderline transactions go to investigators who can approve, decline or override.'}
- {capability: model-governance, level: 3, why: 'In regulated firms, models that block payments fall under model risk management with documented validation.'}
- capability: decision-management
  level: 3
  why: Scores, rules and thresholds combine into approve, decline or refer outcomes that are versioned, tested against past cases and logged with reasons.
- {capability: model-lineage, level: 3, why: 'Model risk reviews and disputes need each model version traced to its training data, features and code.'}
benefits_from:
- {capability: shadow-deployment, why: Test new models on live traffic without blocking payments.}
- {capability: champion-challenger, why: Promote a challenger only once it beats the live model on real transactions.}
- {capability: graph-data, why: 'Exposes rings of linked accounts, devices and merchants.'}
- {capability: entity-resolution, why: Links identities that fraudsters spread across accounts.}
- {capability: data-labelling, why: Turns investigator decisions into labelled training data quickly.}
- {capability: continuous-training, why: Shortens the time between a new fraud pattern and an updated model.}
- {capability: cross-region-failover, why: Keeps scoring available when a region fails.}
- {capability: elastic-scaling, why: Absorbs seasonal peaks in transaction volume.}
- {capability: streaming-sql, why: Lets fraud analysts write new velocity features without stream-processing code.}
personas:
- persona-data-scientist
- persona-ml-engineer
- persona-data-engineer
- persona-software-engineer
- persona-risk-compliance
- persona-platform-engineer
patterns: [fti-pipelines, kappa-architecture, lambda-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Card payments, transfers, account openings and insurance claims are attacked continuously, and fraud has to be stopped before money moves. Each transaction is scored as it happens by a model that combines the transaction itself with recent behaviour, such as how many payments this card made in the last ten minutes, computed from streams and served from an online store. The score, together with rules, decides whether to approve, decline or send the transaction to an investigator, all within the authorisation time limit.

Good looks like most fraud stopped at the point of payment, few genuine customers declined, decisions explainable to investigators, customers and regulators, and models updated quickly as fraud patterns change. Confirmed fraud labels often arrive weeks later through chargebacks, so monitoring cannot rely on accuracy alone.

# Non-functional requirements

- 99th-percentile scoring latency within the authorisation budget, often under 50 milliseconds including feature lookup.
- Availability of 99.95 per cent or higher, with fallback rules if the model cannot be reached.
- Behaviour features reflect transactions within seconds.
- Peak throughput of thousands of transactions per second.
- Decision records retained for the dispute and regulatory period, often several years.

# Risks

- Features computed differently in training and in the live stream make the model behave unpredictably.
- Chargebacks arrive weeks late, hiding a decline in detection.
- High false-positive rates decline genuine customers and lose revenue.
- An outage in scoring either blocks payments or lets everything through.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Real-time inference](../capabilities/mlops/real-time-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Scores must return within the payment authorisation window, typically tens of milliseconds. |
| [Online feature store](../capabilities/machine-learning/online-feature-store.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Recent-behaviour features for each card or account must be read in milliseconds at scoring time. |
| [Stream processing](../capabilities/processing/stream-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 3 (Defined) | Counts and amounts over sliding windows are computed continuously from the transaction stream. |
| [Event streaming](../capabilities/ingestion-integration/event-streaming.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Transactions and outcomes flow as durable, replayable events between payment systems, features and models. |
| [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Training must use features as they stood at each transaction, or the model will not behave the same live. |
| [Model training](../capabilities/machine-learning/model-training.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Models are retrained regularly on recent labelled fraud. |
| [Model registry](../capabilities/machine-learning/model-registry.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | The version scoring live payments must be controlled, approved and quick to roll back. |
| [Inference logging](../capabilities/mlops/inference-logging.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Every decision, with its inputs, model version and score, is kept for disputes, audit and retraining. |
| [Drift detection](../capabilities/mlops/drift-detection.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Fraudsters adapt, so changes in inputs and scores must be caught before labels arrive. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Detection and false-positive rates are tracked as confirmed fraud and chargebacks come in. |
| [Model explainability](../capabilities/machine-learning/model-explainability.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Investigators and customers need reason codes for declines. |
| [Human oversight of AI](../capabilities/governance/human-oversight.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Borderline transactions go to investigators who can approve, decline or override. |
| [Model governance](../capabilities/mlops/model-governance.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | In regulated firms, models that block payments fall under model risk management with documented validation. |
| [Decision management](../capabilities/serving/decision-management.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Scores, rules and thresholds combine into approve, decline or refer outcomes that are versioned, tested against past cases and logged with reasons. |
| [Model lineage](../capabilities/metadata/model-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Model risk reviews and disputes need each model version traced to its training data, features and code. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Shadow deployment](../capabilities/mlops/shadow-deployment.md) | Test new models on live traffic without blocking payments. |
| [Champion-challenger](../capabilities/mlops/champion-challenger.md) | Promote a challenger only once it beats the live model on real transactions. |
| [Graph data](../capabilities/specialised-data/graph-data.md) | Exposes rings of linked accounts, devices and merchants. |
| [Entity resolution](../capabilities/master-data/entity-resolution.md) | Links identities that fraudsters spread across accounts. |
| [Data labelling](../capabilities/machine-learning/data-labelling.md) | Turns investigator decisions into labelled training data quickly. |
| [Continuous training](../capabilities/mlops/continuous-training.md) | Shortens the time between a new fraud pattern and an updated model. |
| [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md) | Keeps scoring available when a region fails. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | Absorbs seasonal peaks in transaction volume. |
| [Streaming SQL](../capabilities/processing/streaming-sql.md) | Lets fraud analysts write new velocity features without stream-processing code. |

# Personas

- [Data scientist](../personas/persona-data-scientist.md): Explores data and builds statistical and machine learning models.
- [ML engineer](../personas/persona-ml-engineer.md): Takes models to production and keeps them running reliably.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.
- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.

# Patterns

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)
- [Kappa architecture](../patterns/kappa-architecture.md)
- [Lambda architecture](../patterns/lambda-architecture.md)

# Frameworks that apply

- [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md): Google Cloud's three-level description of how far an organisation has automated the building, training and release of machine learning systems.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 9 of 15 | [Inference logging](../capabilities/mlops/inference-logging.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Decision management](../capabilities/serving/decision-management.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 14 of 15 | [Decision management](../capabilities/serving/decision-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 12 of 15 | [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Decision management](../capabilities/serving/decision-management.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 15 (+1 in preview) | [Stream processing](../capabilities/processing/stream-processing.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Decision management](../capabilities/serving/decision-management.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md) (preview only) |
| [Databricks](../platforms/platform-databricks.md) | 12 of 15 | [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Decision management](../capabilities/serving/decision-management.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 0 of 15 | [Real-time inference](../capabilities/mlops/real-time-inference.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Stream processing](../capabilities/processing/stream-processing.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model governance](../capabilities/mlops/model-governance.md), [Decision management](../capabilities/serving/decision-management.md), [Model lineage](../capabilities/metadata/model-lineage.md) |
| [Informatica](../platforms/platform-informatica.md) | 1 of 15 | [Real-time inference](../capabilities/mlops/real-time-inference.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Stream processing](../capabilities/processing/stream-processing.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Decision management](../capabilities/serving/decision-management.md), [Model lineage](../capabilities/metadata/model-lineage.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 7 of 15 | [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Decision management](../capabilities/serving/decision-management.md) |
| [Oracle](../platforms/platform-oracle.md) | 6 of 15 | [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model governance](../capabilities/mlops/model-governance.md), [Decision management](../capabilities/serving/decision-management.md), [Model lineage](../capabilities/metadata/model-lineage.md) |
| [SAP](../platforms/platform-sap.md) | 2 of 15 | [Real-time inference](../capabilities/mlops/real-time-inference.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Stream processing](../capabilities/processing/stream-processing.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model governance](../capabilities/mlops/model-governance.md), [Decision management](../capabilities/serving/decision-management.md), [Model lineage](../capabilities/metadata/model-lineage.md) |
| [Teradata](../platforms/platform-teradata.md) | 5 of 15 (+1 in preview) | [Real-time inference](../capabilities/mlops/real-time-inference.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Stream processing](../capabilities/processing/stream-processing.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Decision management](../capabilities/serving/decision-management.md), [Model lineage](../capabilities/metadata/model-lineage.md), [Human oversight of AI](../capabilities/governance/human-oversight.md) (preview only) |
| [IBM](../platforms/platform-ibm.md) | 7 of 15 | [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Human oversight of AI](../capabilities/governance/human-oversight.md), [Decision management](../capabilities/serving/decision-management.md), [Model lineage](../capabilities/metadata/model-lineage.md) |
| [Palantir](../platforms/platform-palantir.md) | 6 of 15 | [Real-time inference](../capabilities/mlops/real-time-inference.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Event streaming](../capabilities/ingestion-integration/event-streaming.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Drift detection](../capabilities/mlops/drift-detection.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Decision management](../capabilities/serving/decision-management.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 11 of 15 | [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model governance](../capabilities/mlops/model-governance.md), [Decision management](../capabilities/serving/decision-management.md), [Model lineage](../capabilities/metadata/model-lineage.md) |
| [Independent vendors](../platforms/platform-independent.md) | 12 of 15 | [Real-time inference](../capabilities/mlops/real-time-inference.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Inference logging](../capabilities/mlops/inference-logging.md) |
