---
type: Use Case
id: usecase-recommendations
title: Personalised recommendations
description: Recommend products or content to each user in real time.
aliases: [next best offer, personalisation]
requires:
- capability: behavioural-event-collection
  level: 3
  why: Views, clicks and purchases from every app and site are the main training signal and must follow one tracking plan.
- {capability: streaming-ingestion, level: 2, why: Session behaviour must reach features within seconds to affect the next page.}
- {capability: feature-engineering, level: 2, why: 'Events are turned into user, item and context features.'}
- {capability: model-training, level: 2, why: Retrieval and ranking models are trained on large interaction histories.}
- {capability: vector-search, level: 2, why: Candidates are found by nearest-neighbour search over item and user embeddings.}
- {capability: online-feature-store, level: 3, why: Session and user features must be read in milliseconds at request time.}
- {capability: real-time-inference, level: 3, why: Ranking runs on every page or screen request within its latency budget.}
- {capability: low-latency-serving, level: 3, why: Precomputed candidates and fallback lists are served in milliseconds.}
- {capability: canary-ab-testing, level: 3, why: Only live experiments show whether a new model increases sales or engagement.}
- {capability: inference-logging, level: 3, why: Logged impressions and clicks are needed for training and to correct for what was shown.}
- {capability: continuous-training, level: 3, why: 'Catalogues and tastes change daily, so models must be retrained on a frequent schedule.'}
- {capability: model-registry, level: 2, why: Versions in experiments and in production must be tracked and reversible.}
- {capability: consent-management, level: 2, why: Personalisation must respect tracking and profiling consent.}
benefits_from:
- {capability: embedding-generation, why: Gives new items useful representations from text and images before anyone interacts with them.}
- {capability: gpu-compute, why: Shortens training of large retrieval and ranking models.}
- {capability: distributed-training, why: Handles interaction histories too large for one machine.}
- {capability: product-information-management, why: Clean product attributes and availability prevent recommending items that cannot be bought.}
- {capability: offline-feature-store, why: Keeps training features consistent with those served online.}
- {capability: shadow-deployment, why: Checks latency and outputs on live traffic before an experiment starts.}
- {capability: stream-processing, why: Computes session features continuously.}
- {capability: elastic-scaling, why: Handles traffic peaks during sales and launches.}
- {capability: experimentation, why: 'Shared assignment, guardrail metrics and statistical methods make model tests comparable with other product experiments.'}
personas:
- persona-data-scientist
- persona-ml-engineer
- persona-software-engineer
- persona-data-engineer
- persona-data-product-owner
patterns: [fti-pipelines, lambda-architecture, kappa-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Retailers, media services and marketplaces recommend products, articles or videos to increase sales, engagement or retention. Clicks, views and purchases are collected from apps and websites, turned into features and embeddings, and used to train models that find likely candidates and rank them for each user. At request time a service fetches the user's latest session features, retrieves candidates, ranks them and returns a list within the page's response time, while every impression and click is logged to train the next version.

Good looks like recommendations that respond to what the user did a few seconds ago, measurable uplift in A/B tests against the current approach, sensible results for new users and new items, and never recommending something unavailable or unsuitable. Offline accuracy is a poor guide to business effect, so online experiments decide releases.

# Non-functional requirements

- Recommendations return within 50 to 100 milliseconds at page-load concurrency.
- Session events affect recommendations within seconds.
- A fallback list, such as popular items, is served if the model service fails.
- Experiment results have enough traffic and duration to be statistically sound.

# Risks

- Feedback loops, where the model only learns from what it already showed, narrow recommendations over time.
- New users and new items get poor recommendations.
- Offline metric gains do not translate into business uplift.
- Unavailable, inappropriate or restricted items are recommended.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Views, clicks and purchases from every app and site are the main training signal and must follow one tracking plan. |
| [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 2 (Managed) | Session behaviour must reach features within seconds to affect the next page. |
| [Feature engineering](../capabilities/machine-learning/feature-engineering.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Events are turned into user, item and context features. |
| [Model training](../capabilities/machine-learning/model-training.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Retrieval and ranking models are trained on large interaction histories. |
| [Vector search](../capabilities/generative-ai/vector-search.md) | [Generative AI](../capabilities/generative-ai/generative-ai.md) | 2 (Managed) | Candidates are found by nearest-neighbour search over item and user embeddings. |
| [Online feature store](../capabilities/machine-learning/online-feature-store.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Session and user features must be read in milliseconds at request time. |
| [Real-time inference](../capabilities/mlops/real-time-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Ranking runs on every page or screen request within its latency budget. |
| [Low-latency serving](../capabilities/serving/low-latency-serving.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Precomputed candidates and fallback lists are served in milliseconds. |
| [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Only live experiments show whether a new model increases sales or engagement. |
| [Inference logging](../capabilities/mlops/inference-logging.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Logged impressions and clicks are needed for training and to correct for what was shown. |
| [Continuous training](../capabilities/mlops/continuous-training.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Catalogues and tastes change daily, so models must be retrained on a frequent schedule. |
| [Model registry](../capabilities/machine-learning/model-registry.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Versions in experiments and in production must be tracked and reversible. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Personalisation must respect tracking and profiling consent. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Embedding generation](../capabilities/generative-ai/embedding-generation.md) | Gives new items useful representations from text and images before anyone interacts with them. |
| [GPU and accelerated compute](../capabilities/compute/gpu-compute.md) | Shortens training of large retrieval and ranking models. |
| [Distributed training](../capabilities/machine-learning/distributed-training.md) | Handles interaction histories too large for one machine. |
| [Product information management](../capabilities/master-data/product-information-management.md) | Clean product attributes and availability prevent recommending items that cannot be bought. |
| [Offline feature store](../capabilities/machine-learning/offline-feature-store.md) | Keeps training features consistent with those served online. |
| [Shadow deployment](../capabilities/mlops/shadow-deployment.md) | Checks latency and outputs on live traffic before an experiment starts. |
| [Stream processing](../capabilities/processing/stream-processing.md) | Computes session features continuously. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | Handles traffic peaks during sales and launches. |
| [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md) | Shared assignment, guardrail metrics and statistical methods make model tests comparable with other product experiments. |

# Personas

- [Data scientist](../personas/persona-data-scientist.md): Explores data and builds statistical and machine learning models.
- [ML engineer](../personas/persona-ml-engineer.md): Takes models to production and keeps them running reliably.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.

# Patterns

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)
- [Lambda architecture](../patterns/lambda-architecture.md)
- [Kappa architecture](../patterns/kappa-architecture.md)

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 10 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 10 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 11 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 13 (+1 in preview) | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md) (preview only) |
| [Databricks](../platforms/platform-databricks.md) | 10 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 3 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Informatica](../platforms/platform-informatica.md) | 1 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 6 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Oracle](../platforms/platform-oracle.md) | 5 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [SAP](../platforms/platform-sap.md) | 1 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Model training](../capabilities/machine-learning/model-training.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Teradata](../platforms/platform-teradata.md) | 4 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Streaming ingestion](../capabilities/ingestion-integration/streaming-ingestion.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Low-latency serving](../capabilities/serving/low-latency-serving.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [IBM](../platforms/platform-ibm.md) | 5 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Vector search](../capabilities/generative-ai/vector-search.md), [Online feature store](../capabilities/machine-learning/online-feature-store.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 9 of 13 | [Behavioural event collection](../capabilities/ingestion-integration/behavioural-event-collection.md), [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Continuous training](../capabilities/mlops/continuous-training.md), [Consent and purpose management](../capabilities/governance/consent-management.md) |
| [Independent vendors](../platforms/platform-independent.md) | 8 of 13 | [Feature engineering](../capabilities/machine-learning/feature-engineering.md), [Real-time inference](../capabilities/mlops/real-time-inference.md), [Canary and A/B testing](../capabilities/mlops/canary-ab-testing.md), [Inference logging](../capabilities/mlops/inference-logging.md), [Continuous training](../capabilities/mlops/continuous-training.md) |
