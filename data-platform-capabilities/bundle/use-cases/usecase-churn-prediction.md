---
type: Use Case
id: usecase-churn-prediction
title: Churn prediction
description: Score customers regularly by likelihood to leave so teams can act before they do.
aliases: [attrition prediction, customer retention, churn early warning]
requires:
- {capability: feature-engineering, level: 2, why: 'Raw billing, usage and contact data has to become consistent customer-level features.'}
- {capability: point-in-time-joins, level: 3, why: 'Training features must be as known before each customer left, or the model learns from the future.'}
- {capability: model-training, level: 2, why: Models are trained and retrained on customer history.}
- {capability: experiment-tracking, level: 2, why: 'Model versions, features and results must be comparable and reproducible.'}
- {capability: model-evaluation, level: 2, why: 'Models are judged on ranking quality and expected uplift, not only on accuracy.'}
- {capability: model-explainability, level: 2, why: Retention teams need the main reasons behind each score to choose the right action.}
- {capability: model-registry, level: 2, why: The approved model version used for scoring must be clear and reversible.}
- {capability: batch-inference, level: 3, why: The whole active customer base is scored on a schedule within a fixed window.}
- {capability: workflow-orchestration, level: 2, why: 'Feature refresh, scoring and delivery run in order on every cycle.'}
- {capability: reverse-etl, level: 2, why: Scores are useful only once they reach the CRM and campaign tools where retention teams act.}
- {capability: model-performance-monitoring, level: 2, why: Actual churn arrives weeks later and must be compared with past scores to spot decline.}
- {capability: consent-management, level: 2, why: Profiling and retention contact must stay within permitted purposes and opt-outs.}
- capability: experimentation
  level: 2
  why: Retention uplift is measured against a randomly held-out control group, which the use case names as what good looks like.
benefits_from:
- {capability: offline-feature-store, why: Shares customer features with other models such as upsell and credit risk.}
- {capability: automl, why: Gives a quick baseline to beat.}
- {capability: pretrained-predictive-models, why: Gives usable scores before enough history exists to train a dedicated model.}
- {capability: drift-detection, why: 'Warns when customer behaviour shifts, such as after a price change, before outcomes are known.'}
- {capability: champion-challenger, why: Tests new models against the current one on live scoring cycles.}
- {capability: behavioural-event-collection, why: Digital engagement is often the earliest signal that a customer is drifting away.}
- {capability: master-data-management, why: One customer record avoids scoring duplicates separately.}
- {capability: fairness-assessment, why: Checks that retention offers are not withheld unfairly from groups of customers.}
- {capability: continuous-training, why: Retrains automatically as products and pricing change.}
- capability: streaming-inference
  why: An early-warning variant scores customers within minutes of signals such as a cancellation-page visit, a complaint or a failed payment.
- {capability: stream-processing, why: Keeps rolling engagement and service features current between batch scoring runs.}
- {capability: online-feature-store, why: Serves the latest customer features to event-triggered scoring.}
- {capability: data-alerting, why: Notifies the retention team when a customer's score crosses a threshold instead of waiting for the next campaign cycle.}
personas:
- persona-data-scientist
- persona-ml-engineer
- persona-data-engineer
- persona-business-user
- persona-data-product-owner
patterns: [fti-pipelines, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Keeping a customer usually costs less than winning a new one, but retention offers are expensive when they go to customers who would have stayed anyway. Churn prediction scores each customer, usually daily or weekly, on how likely they are to leave within a set period, from billing, usage, service contacts and behaviour. Data scientists build training sets with features as they were known at each point in the past, train and evaluate models, and a batch pipeline scores the whole customer base and sends scores and reasons to CRM and campaign tools.

Good looks like scores that arrive in retention teams' tools before each campaign cycle, a reason attached to each score so the action fits the customer, and retention measured against a control group so the business sees the uplift the model produces, not only its accuracy. The definition of churn itself must be agreed first, especially where customers do not cancel a contract but simply stop buying.

# Non-functional requirements

- Scores are refreshed daily or weekly, ahead of the campaign cycle.
- The full active base, often millions of customers, is scored within the batch window.
- Scores and reasons are in CRM by the start of the business day.
- Training runs can be reproduced from recorded data, code and parameters.

# Risks

- Leakage of future information gives a model that looks accurate offline and fails in use.
- Scores are ignored because they arrive outside the tools staff use or carry no reasons.
- Success is measured by accuracy rather than retention uplift, so offers go to customers who would have stayed.
- An unclear churn definition, especially without contracts, makes labels inconsistent.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Feature engineering](../capabilities/machine-learning/feature-engineering.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Raw billing, usage and contact data has to become consistent customer-level features. |
| [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Training features must be as known before each customer left, or the model learns from the future. |
| [Model training](../capabilities/machine-learning/model-training.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Models are trained and retrained on customer history. |
| [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Model versions, features and results must be comparable and reproducible. |
| [Model evaluation](../capabilities/machine-learning/model-evaluation.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Models are judged on ranking quality and expected uplift, not only on accuracy. |
| [Model explainability](../capabilities/machine-learning/model-explainability.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Retention teams need the main reasons behind each score to choose the right action. |
| [Model registry](../capabilities/machine-learning/model-registry.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | The approved model version used for scoring must be clear and reversible. |
| [Batch inference](../capabilities/mlops/batch-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | The whole active customer base is scored on a schedule within a fixed window. |
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | 2 (Managed) | Feature refresh, scoring and delivery run in order on every cycle. |
| [Reverse ETL](../capabilities/serving/reverse-etl.md) | [Serving and activation](../capabilities/serving/serving.md) | 2 (Managed) | Scores are useful only once they reach the CRM and campaign tools where retention teams act. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | [ML operations](../capabilities/mlops/mlops.md) | 2 (Managed) | Actual churn arrives weeks later and must be compared with past scores to spot decline. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Profiling and retention contact must stay within permitted purposes and opt-outs. |
| [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 (Managed) | Retention uplift is measured against a randomly held-out control group, which the use case names as what good looks like. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Offline feature store](../capabilities/machine-learning/offline-feature-store.md) | Shares customer features with other models such as upsell and credit risk. |
| [AutoML](../capabilities/machine-learning/automl.md) | Gives a quick baseline to beat. |
| [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md) | Gives usable scores before enough history exists to train a dedicated model. |
| [Drift detection](../capabilities/mlops/drift-detection.md) | Warns when customer behaviour shifts, such as after a price change, before outcomes are known. |
| [Champion-challenger](../capabilities/mlops/champion-challenger.md) | Tests new models against the current one on live scoring cycles. |
| [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md) | Digital engagement is often the earliest signal that a customer is drifting away. |
| [Master data management](../capabilities/master-data/master-data-management.md) | One customer record avoids scoring duplicates separately. |
| [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) | Checks that retention offers are not withheld unfairly from groups of customers. |
| [Continuous training](../capabilities/mlops/continuous-training.md) | Retrains automatically as products and pricing change. |
| [Streaming inference](../capabilities/mlops/streaming-inference.md) | An early-warning variant scores customers within minutes of signals such as a cancellation-page visit, a complaint or a failed payment. |
| [Stream processing](../capabilities/processing/stream-processing.md) | Keeps rolling engagement and service features current between batch scoring runs. |
| [Online feature store](../capabilities/machine-learning/online-feature-store.md) | Serves the latest customer features to event-triggered scoring. |
| [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md) | Notifies the retention team when a customer's score crosses a threshold instead of waiting for the next campaign cycle. |

# Personas

- [Data scientist](../personas/persona-data-scientist.md): Explores data and builds statistical and machine learning models.
- [ML engineer](../personas/persona-ml-engineer.md): Takes models to production and keeps them running reliably.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.

# Patterns

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)
- [Medallion architecture](../patterns/medallion-architecture.md)

# Frameworks that apply

- [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md): Google Cloud's three-level description of how far an organisation has automated the building, training and release of machine learning systems.
- [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md): A five-level model from Microsoft that describes MLOps maturity across people, model creation, model release and application integration.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 9 of 13 | [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 10 of 13 | [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 10 of 13 | [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 13 | [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Databricks](../platforms/platform-databricks.md) | 10 of 13 | [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 1 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Informatica](../platforms/platform-informatica.md) | 2 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 4 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Oracle](../platforms/platform-oracle.md) | 5 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [SAP](../platforms/platform-sap.md) | 1 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Model training](../capabilities/machine-learning/model-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Teradata](../platforms/platform-teradata.md) | 5 of 13 | [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [IBM](../platforms/platform-ibm.md) | 3 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Palantir](../platforms/platform-palantir.md) | 3 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 9 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Reverse ETL](../capabilities/serving/reverse-etl.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Independent vendors](../platforms/platform-independent.md) | 9 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Point-in-time correct joins](../capabilities/machine-learning/point-in-time-joins.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) |
